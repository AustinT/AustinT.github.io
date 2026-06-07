#!/usr/bin/env python3
"""Generate per-paper Quarto pages from BibTeX files in the publications submodule.

Run after adding new papers to the publications submodule:
    python scripts/generate_paper_pages.py

Existing pages are never overwritten — add your retrospective content freely.
If a BibTeX field contains a LaTeX sequence not in the lookup tables, the script
raises an error pointing to the exact entry and field to fix before re-running.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PAPERS_DIR = REPO_ROOT / "src" / "research" / "papers"
PUBS_DIR = REPO_ROOT / "publications"

BIB_FILES: dict[str, str] = {
    "papers.bib": "paper",
    "workshops.bib": "workshop",
    "preprints.bib": "preprint",
}


# ---- LaTeX → Unicode resolution ----

# Map (accent_command_char, letter) → unicode character
_ACCENT_MAP: dict[tuple[str, str], str] = {
    # acute (')
    ("'", "a"): "á", ("'", "e"): "é", ("'", "i"): "í",
    ("'", "o"): "ó", ("'", "u"): "ú", ("'", "y"): "ý",
    ("'", "A"): "Á", ("'", "E"): "É", ("'", "I"): "Í",
    ("'", "O"): "Ó", ("'", "U"): "Ú", ("'", "Y"): "Ý",
    # grave (`)
    ("`", "a"): "à", ("`", "e"): "è", ("`", "i"): "ì",
    ("`", "o"): "ò", ("`", "u"): "ù",
    ("`", "A"): "À", ("`", "E"): "È", ("`", "I"): "Ì",
    ("`", "O"): "Ò", ("`", "U"): "Ù",
    # umlaut (")
    ('"', "a"): "ä", ('"', "e"): "ë", ('"', "i"): "ï",
    ('"', "o"): "ö", ('"', "u"): "ü", ('"', "y"): "ÿ",
    ('"', "A"): "Ä", ('"', "E"): "Ë", ('"', "I"): "Ï",
    ('"', "O"): "Ö", ('"', "U"): "Ü",
    # circumflex (^)
    ("^", "a"): "â", ("^", "e"): "ê", ("^", "i"): "î",
    ("^", "o"): "ô", ("^", "u"): "û",
    ("^", "A"): "Â", ("^", "E"): "Ê", ("^", "I"): "Î",
    ("^", "O"): "Ô", ("^", "U"): "Û",
    # tilde (~)
    ("~", "a"): "ã", ("~", "n"): "ñ", ("~", "o"): "õ",
    ("~", "A"): "Ã", ("~", "N"): "Ñ", ("~", "O"): "Õ",
    # cedilla (c)
    ("c", "c"): "ç", ("c", "C"): "Ç",
}

# Standalone commands with no letter argument
_COMMAND_MAP: dict[str, str] = {
    "ss": "ß",
    "ae": "æ", "AE": "Æ",
    "oe": "œ", "OE": "Œ",
    "aa": "å", "AA": "Å",
    "o": "ø", "O": "Ø",
    "l": "ł", "L": "Ł",
}

# Matches accent sequences in all common BibTeX forms:
#   {\'a}   \'{a}   \'a   {\ss}   \ss
_LATEX_RE = re.compile(
    r"\{\\(?P<a1>[`'\"^~c])(?P<l1>[a-zA-Z])\}"   # {\'a}
    r"|\\(?P<a2>[`'\"^~c])\{(?P<l2>[a-zA-Z])\}"  # \'{a}
    r"|\\(?P<a3>[`'\"^~c])(?P<l3>[a-zA-Z])"      # \'a
    r"|\{\\(?P<cmd1>[a-zA-Z]+)\}"                 # {\ss}
    r"|\\(?P<cmd2>[a-zA-Z]+)(?=[^a-zA-Z]|$)"     # \ss
)


def _resolve_latex(entry_id: str, field: str, value: str) -> str:
    """Replace known LaTeX sequences with Unicode. Raise on anything unknown."""
    if "\\" not in value:
        return value

    # Pass 1: strip multi-letter formatting commands (\textsc{X} → X).
    # Uses ≥4-letter names to avoid colliding with short accent commands (c, o, l…).
    value = re.sub(r"\\[a-zA-Z]{4,}\{([^}]*)\}", r"\1", value)

    # Pass 2: replace accent sequences and short commands.
    def _replace(m: re.Match) -> str:
        accent = m.group("a1") or m.group("a2") or m.group("a3")
        letter = m.group("l1") or m.group("l2") or m.group("l3")
        cmd = m.group("cmd1") or m.group("cmd2")

        if accent is not None:
            key = (accent, letter)
            if key in _ACCENT_MAP:
                return _ACCENT_MAP[key]
            raise ValueError(
                f"Unknown LaTeX accent '\\{accent}{letter}' in "
                f"entry '{entry_id}', field '{field}'.\n"
                f"  Add it to _ACCENT_MAP or convert to Unicode in the .bib file."
            )
        if cmd in _COMMAND_MAP:
            return _COMMAND_MAP[cmd]
        raise ValueError(
            f"Unknown LaTeX command '\\{cmd}' in "
            f"entry '{entry_id}', field '{field}'.\n"
            f"  Add it to _COMMAND_MAP or convert to Unicode in the .bib file."
        )

    value = _LATEX_RE.sub(_replace, value)

    # Strip remaining grouping braces (e.g. {Coley, Connor W} used to protect names).
    value = value.replace("{", "").replace("}", "")

    # Any remaining backslash is an unrecognised LaTeX sequence.
    m = re.search(r"\\.", value)
    if m:
        raise ValueError(
            f"Unhandled LaTeX sequence {m.group()!r} in "
            f"entry '{entry_id}', field '{field}'.\n"
            f"  Convert to Unicode in the .bib file or add handling to the script."
        )

    return value


def _resolve_entry(entry: dict[str, str]) -> dict[str, str]:
    """Return entry with all field values resolved to Unicode."""
    entry_id = entry.get("ID", "?")
    resolved: dict[str, str] = {}
    for field, value in entry.items():
        resolved[field] = (
            value if field in ("ID", "ENTRYTYPE")
            else _resolve_latex(entry_id, field, value)
        )
    return resolved


# ---- BibTeX parser ----

def _extract_braced(text: str, start: int) -> tuple[str, int]:
    """Return (content_inside_braces, index_after_closing_brace).
    start must point at '{'. Handles arbitrarily nested braces.
    """
    assert text[start] == "{", f"Expected '{{' at position {start}"
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1 : i], i + 1
    raise ValueError(f"Unmatched '{{' at position {start}")


def _parse_fields(content: str) -> dict[str, str]:
    """Parse 'key, field = value, …' body of a BibTeX entry into a field dict."""
    fields: dict[str, str] = {}

    m = re.match(r"\s*([^\s,]+)\s*,", content)
    if not m:
        return fields
    fields["ID"] = m.group(1)
    pos = m.end()

    while pos < len(content):
        while pos < len(content) and content[pos] in " \t\n\r,":
            pos += 1
        if pos >= len(content):
            break

        fm = re.match(r"([a-zA-Z_]\w*)\s*=\s*", content[pos:])
        if not fm:
            break
        name = fm.group(1).lower()
        pos += fm.end()

        if pos >= len(content):
            break

        ch = content[pos]
        if ch == "{":
            value, pos = _extract_braced(content, pos)
        elif ch == '"':
            end = pos + 1
            while end < len(content) and content[end] != '"':
                end += 1
            value = content[pos + 1 : end]
            pos = end + 1
        else:
            bm = re.match(r"([^\s,}]+)", content[pos:])
            if not bm:
                break
            value = bm.group(1)
            pos += bm.end()

        fields[name] = value

    return fields


def parse_bib(path: Path) -> list[dict[str, str]]:
    """Parse a .bib file and return a list of entry field dicts."""
    text = path.read_text(encoding="utf-8")
    entries = []
    pos = 0
    while pos < len(text):
        at = text.find("@", pos)
        if at == -1:
            break
        m = re.match(r"@(\w+)\s*\{", text[at:])
        if not m:
            pos = at + 1
            continue
        entry_type = m.group(1).lower()
        brace_start = at + m.end() - 1
        content, pos = _extract_braced(text, brace_start)
        if entry_type in ("comment", "string", "preamble"):
            continue
        fields = _parse_fields(content)
        fields["ENTRYTYPE"] = entry_type
        entries.append(fields)
    return entries


# ---- Page generation ----

def _format_authors(raw: str) -> str:
    authors = []
    for part in raw.split(" and "):
        part = part.strip()
        if "," in part:
            last, first = part.split(",", 1)
            part = f"{first.strip()} {last.strip()}"
        authors.append(part)
    return ", ".join(authors)


def _get_url(entry: dict[str, str]) -> str:
    if entry.get("url"):
        return entry["url"]
    if entry.get("doi"):
        return f"https://doi.org/{entry['doi']}"
    m = re.search(r"arXiv:(\d{4}\.\d+)", entry.get("journal", ""))
    if m:
        return f"https://arxiv.org/abs/{m.group(1)}"
    return ""


def _get_venue(entry: dict[str, str]) -> str:
    raw = entry.get("booktitle") or entry.get("journal") or ""
    return re.sub(r"arXiv preprint arXiv:\d{4}\.\d+", "arXiv preprint", raw)


def _make_qmd(entry: dict[str, str], category: str) -> str:
    title = entry.get("title", "Untitled").replace('"', "'")
    year = entry.get("year", "2000")
    month_map = {
        "jan": "01", "feb": "02", "mar": "03", "apr": "04",
        "may": "05", "jun": "06", "jul": "07", "aug": "08",
        "sep": "09", "oct": "10", "nov": "11", "dec": "12",
    }
    month = month_map.get(entry.get("month", "").lower()[:3], "01")

    authors = _format_authors(entry.get("author", ""))
    venue = _get_venue(entry)
    url = _get_url(entry)
    authoritative_url = entry.get("authoritative_link", "")

    fm = [
        "---",
        f'title: "{title}"',
        f"year: {year}",
        "order: 999999",
    ]
    if authors:
        fm.append(f'authors: "{authors}"')
    if venue:
        fm.append(f'venue: "{venue}"')
    if authoritative_url:
        fm.append(f'authoritative_url: "{authoritative_url}"')
    if url:
        fm.append(f'paper_url: "{url}"')
    fm.append(f"categories: [{category}]")
    fm.append("---")

    body = ""
    if authoritative_url and url:
        body += (
            f"[Official version]({url}){{.btn .btn-outline-primary .btn-sm}} "
            f"[Version I consider authoritative]({authoritative_url}){{.btn .btn-primary .btn-sm}}\n\n"
        )
    elif authoritative_url:
        body += f"[Read the paper]({authoritative_url}){{.btn .btn-primary .btn-sm}}\n\n"
    elif url:
        body += f"[Read the paper]({url}){{.btn .btn-primary .btn-sm}}\n\n"
    body += "## Summary\n\n<!-- TODO --> (no content here yet)\n\n"
    body += "## My contribution\n\n<!-- TODO --> (no content here yet)\n\n"
    body += "## Thoughts\n\n<!-- TODO --> (no content here yet)\n"

    return "\n".join(fm) + "\n\n" + body


# ---- Main ----

def main() -> None:
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    created: list[str] = []
    skipped: list[str] = []

    for bib_file, category in BIB_FILES.items():
        bib_path = PUBS_DIR / bib_file
        if not bib_path.exists():
            raise FileNotFoundError(
                f"{bib_path} not found.\n"
                f"  Run: git submodule update --init"
            )

        entries = parse_bib(bib_path)
        for entry in entries:
            entry = _resolve_entry(entry)  # raises on unknown LaTeX
            entry_id = entry.get("ID", "?")

            # --- website_exclude ---
            if "website_exclude" not in entry:
                print(
                    f"\n{'!' * 60}\n"
                    f"WARNING: entry '{entry_id}' in {bib_file} has no website_exclude field.\n"
                    f"Assuming website_exclude=true (skipping). Add the field to remove this warning.\n"
                    f"{'!' * 60}\n",
                    file=sys.stderr,
                )
                continue

            exclude_raw = entry["website_exclude"].strip().lower()
            if exclude_raw == "true":
                exclude = True
            elif exclude_raw == "false":
                exclude = False
            else:
                raise ValueError(
                    f"Cannot parse website_exclude={entry['website_exclude']!r} "
                    f"in entry '{entry_id}'. Expected 'true' or 'false'."
                )

            if exclude:
                continue

            if "website_slug" not in entry:
                raise ValueError(
                    f"Entry '{entry_id}' has website_exclude=false but no website_slug field."
                )

            slug = entry["website_slug"].strip()
            page_path = PAPERS_DIR / slug / "index.qmd"

            if page_path.exists():
                skipped.append(slug)
                continue

            page_path.parent.mkdir(parents=True, exist_ok=True)
            page_path.write_text(_make_qmd(entry, category))
            created.append(slug)
            print(f"  Created: papers/{slug}/index.qmd")

    print(f"\nDone. Created {len(created)}, skipped {len(skipped)} existing.")


if __name__ == "__main__":
    main()

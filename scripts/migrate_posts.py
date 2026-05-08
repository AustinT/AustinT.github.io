#!/usr/bin/env python3
"""Migrate Nikola markdown posts to Quarto format.

Usage:
    python scripts/migrate_posts.py [--dry-run] [file_or_dir ...]

If no arguments given, migrates all .md files in posts/ (recursively).
Pass individual files or directories to migrate a subset.

For year-directory posts (posts/YYYY/MM/DD/slug.md), the destination slug
is just the filename stem (no date prefix), matching existing Nikola URLs.
For modern posts (posts/YYYY-MM-DD-slug.md), the full filename stem is used.
"""

import argparse
import os
import re
import sys
import textwrap

try:
    import yaml
except ImportError:
    print("PyYAML not found. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


YEAR_DIR_RE = re.compile(r"posts/(\d{4})/(\d{2})/(\d{2})/(.+)\.md$")
MODERN_RE = re.compile(r"posts/(\d{4}-\d{2}-\d{2}-.+)\.md$")


def parse_frontmatter(content: str):
    """Return (frontmatter_dict, body_str). Body includes trailing newline."""
    if not content.startswith("---"):
        return {}, content
    end = content.index("\n---", 3)
    raw_yaml = content[4:end]
    body = content[end + 4:].lstrip("\n")
    fm = yaml.safe_load(raw_yaml) or {}
    return fm, body


def extract_description(body: str) -> str:
    """Extract text before TEASER_END, strip markdown, return ≤200 chars."""
    teaser_end = body.find("<!-- TEASER_END -->")
    if teaser_end == -1:
        text = body
    else:
        text = body[:teaser_end]
    # Strip markdown: inline markup, links, headers, bold/italic
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # [text](url) → text
    text = re.sub(r"[*_]{1,2}([^*_]+)[*_]{1,2}", r"\1", text)  # bold/italic
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)  # headers
    text = re.sub(r"`[^`]+`", "", text)  # inline code
    text = re.sub(r"\[.*?\]", "", text)  # footnote refs
    text = " ".join(text.split())  # collapse whitespace
    text = text.strip()
    if len(text) > 200:
        text = text[:197] + "..."
    return text


def convert_frontmatter(fm: dict) -> dict:
    """Convert Nikola frontmatter keys/values to Quarto equivalents."""
    out = {}
    # Required fields
    if "title" in fm:
        out["title"] = fm["title"]
    if "date" in fm:
        out["date"] = fm["date"]
    # tags → categories
    tags = fm.get("tags") or fm.get("tag") or []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",")]
    if tags:
        out["categories"] = tags
    # Drop: has_math, mathjax, type, link, description (we'll set it), previewimage
    return out


def remove_teaser_comment(body: str) -> str:
    return body.replace("<!-- TEASER_END -->", "").strip() + "\n"


def dest_path(src_path: str, base_output_dir: str) -> str:
    """Compute the output path for a source .md file."""
    norm = src_path.replace("\\", "/")
    year_match = YEAR_DIR_RE.search(norm)
    modern_match = MODERN_RE.search(norm)

    if year_match:
        slug = year_match.group(4)
        return os.path.join(base_output_dir, slug, "index.qmd")
    elif modern_match:
        stem = modern_match.group(1)
        return os.path.join(base_output_dir, stem, "index.qmd")
    else:
        # Fallback: use stem relative to posts/ root
        stem = os.path.splitext(os.path.basename(src_path))[0]
        return os.path.join(base_output_dir, stem, "index.qmd")


def migrate_file(src_path: str, out_path: str, dry_run: bool = False):
    with open(src_path, encoding="utf-8") as f:
        content = f.read()

    fm, body = parse_frontmatter(content)
    description = extract_description(body)
    new_fm = convert_frontmatter(fm)
    if description:
        new_fm["description"] = description
    body = remove_teaser_comment(body)

    # Serialise frontmatter preserving key order and avoiding flow style
    yaml_str = yaml.dump(
        new_fm,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    output = f"---\n{yaml_str}---\n\n{body}"

    if dry_run:
        print(f"  [dry-run] {src_path} → {out_path}")
        return

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"  {src_path} → {out_path}")


def collect_md_files(paths: list[str]) -> list[str]:
    result = []
    for p in paths:
        if os.path.isdir(p):
            for root, _dirs, files in os.walk(p):
                for fn in sorted(files):
                    if fn.endswith(".md"):
                        result.append(os.path.join(root, fn))
        elif os.path.isfile(p) and p.endswith(".md"):
            result.append(p)
    return result


def main():
    parser = argparse.ArgumentParser(description="Migrate Nikola .md posts to Quarto")
    parser.add_argument(
        "paths",
        nargs="*",
        default=["posts/"],
        help="Files or directories to migrate (default: posts/)",
    )
    parser.add_argument(
        "--output-dir",
        default="src/blog",
        help="Base output directory (default: src/blog)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without writing files",
    )
    args = parser.parse_args()

    files = collect_md_files(args.paths)
    if not files:
        print("No .md files found.", file=sys.stderr)
        sys.exit(1)

    print(f"Migrating {len(files)} file(s) to {args.output_dir}/")
    for f in files:
        out = dest_path(f, args.output_dir)
        migrate_file(f, out, dry_run=args.dry_run)
    print("Done.")


if __name__ == "__main__":
    main()

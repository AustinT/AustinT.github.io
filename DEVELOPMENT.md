# Development

Notes on how to work on this website.

## Repository layout

```
src/          # Quarto project root (website source)
scripts/      # Build utilities
decisions/    # Design decision records
publications/ # Git submodule: AustinT/austin-tripp-publications (.bib files)
```

## Checklist for updating the website

1. Edit files in `src/` (usually `.qmd` files).
2. Check that pages render correctly locally: `quarto preview src/`
3. Commit changes on a separate branch, then merge to `src`.
4. Deploy (see below).

## Adding paper pages

Paper pages live in `src/research/papers/` and are scaffolded from the `publications/` submodule
(`github.com/AustinT/austin-tripp-publications`), which contains multiple `.bib` files.

After cloning the repo, initialise the submodule:

```bash
git submodule update --init
```

To generate pages for new `.bib` entries (existing pages are never overwritten):

```bash
python3 scripts/generate_paper_pages.py
```

Each BibTeX entry must have two custom fields or the script will complain:

- `website_exclude = {true|false}` — if absent, the script warns loudly and skips the entry.
  Set to `false` to generate a page; `true` to skip.
- `website_slug = {my-slug}` — required when `website_exclude = false`. Determines the page
  URL (`/research/papers/my-slug/`).

An optional third field controls an extra button on the paper page:

- `authoritative_link = {https://...}` — when present alongside the standard URL/DOI, the page
  shows two buttons: "Authoritative version" and "Official version".

If a `.bib` field contains a LaTeX accent not in the script's lookup table, the script raises
an error identifying the entry and field. Convert it to Unicode in the `.bib` file and re-run.

## Python environment

A top-level uv environment provides numpy, scipy, matplotlib, pandas, and Jupyter for use in blog posts with executable Python cells.

```bash
uv sync          # create/update .venv
uv run quarto preview src/   # preview with the venv active
```

The kernel is registered as `website-blog`. Add `jupyter: website-blog` to a post's frontmatter to execute Python cells. For posts needing different packages, create a per-post uv env and register a separate kernel (see [Per-post Python environments](#per-post-python-environments)).

## How to build/serve locally

```bash
uv run quarto preview src/
```

## How to render (without serving)

```bash
quarto render src/
```

## How to deploy

```bash
quarto publish gh-pages src/ --no-browser
```

This renders the site, runs the post-render redirect script automatically, and pushes
to the `gh-pages` branch. Alternatively, push to the `src` branch to trigger the
GitHub Actions workflow automatically.

To skip CI on a push (e.g. for a README-only change): include `[skip ci]` in the
commit message.

## Adding blog posts

Create `src/blog/YYYY-MM-DD-slug/index.qmd` with frontmatter:

```yaml
---
title: "Post title"
date: YYYY-MM-DD
categories:
    - tag1
    - tag2
description: "One-sentence summary shown in listings."
---
```

Use KaTeX math anywhere — it's enabled globally.

## Redirects

Legacy URLs `/links/` and `/about/` are handled by `scripts/generate_redirects.py`,
which writes meta-refresh HTML into the render output directory after `quarto render`.

## Per-post Python environments

For a post with unique package requirements:

```bash
cd src/blog/YYYY-MM-DD-slug/
uv init --no-package
uv add some-special-package ipykernel
uv run python -m ipykernel install --user --name my-post-kernel
```

Then in the post's frontmatter: `jupyter: my-post-kernel`.

Note: kernel registrations live at `~/.local/share/jupyter/kernels/` and must be re-registered on a new machine.

## My thoughts on some design choices

See `./decisions` for design issues that I've thought through and explanations
of why I made these decisions.

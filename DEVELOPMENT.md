# Development

Notes on how to work on this website.

## Repository layout

```
src/          # Quarto project root (website source)
scripts/      # Build utilities
decisions/    # Design decision records
```

## Checklist for updating the website

1. Edit files in `src/` (usually `.qmd` files).
2. Check that pages render correctly locally: `quarto preview src/`
3. Commit changes on a separate branch, then merge to `src`.
4. Deploy (see below).

## How to build/serve locally

```bash
quarto preview src/
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

## My thoughts on some design choices

See `./decisions` for design issues that I've thought through and explanations
of why I made these decisions.

# Website

This is source code for my personal website. It is a static site built with
Quarto, mostly using Quarto Markdown (`.qmd`) as the source.

## Site structure

- `src/` — Quarto project root (all website source lives here)
  - `src/_quarto.yml` — Quarto configuration (site title, URL, navbar, theme, etc.)
  - `src/index.qmd` — Home page
  - `src/blog/` — Blog posts (one subdirectory per post: `YYYY-MM-DD-slug/index.qmd`)
  - `src/blog/index.qmd` — Blog listing page
  - `src/blog-images/` — Static images served at `/blog-images/`
  - `src/assets/` — Other static assets served at `/assets/`
  - `src/CNAME` — GitHub Pages custom domain file
  - `src/_site/` — **generated output, do not edit directly** (gitignored)
- `scripts/` — Build utilities
  - `scripts/generate_redirects.py` — Post-build: writes legacy redirect HTML files
- `posts/` — Old Nikola blog posts (pending removal after migration)
- `pages/` — Old Nikola pages (pending removal after migration)

## Post frontmatter format

Blog posts use YAML frontmatter like:

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

KaTeX math is enabled globally — no `has_math` field needed.

## Workflow

- Edit `.qmd` files in `src/`
- Preview locally: `quarto preview src/`
- Render: `quarto render src/`
- After rendering, generate redirects: `python scripts/generate_redirects.py --output-dir src/_site`
- Deploy: `quarto publish gh-pages src/ --no-browser`

## Documentation

Any changes to the way the website code is run or managed should be reflected
in README.md or DEVELOPMENT.md

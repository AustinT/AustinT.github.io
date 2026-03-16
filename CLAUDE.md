# Website

This is source code for my personal website. It is a static site built with
nikola, mostly using markdown as the source.

## Site structure

- `posts/` — blog posts (markdown/rst/ipynb with YAML frontmatter)
- `pages/` — static pages (about, CV, resources, etc.)
- `files/` — static assets copied directly to the output
- `conf.py` — Nikola configuration (site title, URL, plugins, etc.)
- `output/` — **generated output, do not edit directly**

There might be some other files/folders with names like "drafts" or "tmp".
These are temporary files and are generally not included in the site.

## Post frontmatter format

Blog posts use YAML frontmatter like:

```yaml
---
title: "Post title"
date: YYYY-MM-DD
tags:
    - tag1
    - tag2
has_math: false
---
```

Use `<!-- TEASER_END -->` to mark where the post preview ends on the index page.

## Workflow

- Edit `.md`/`.rst`/`.ipynb` files in `posts/` or `pages/`, or `conf.py`
- Preview locally: `nikola auto --browser` (requires conda env `nikola`)
- Check for broken links: `nikola check --clean-files`
- Deploy: `nikola github_deploy`
- Commit changes on a separate branch, merge to `src` before deploying

## Python environment

```bash
conda activate nikola
```

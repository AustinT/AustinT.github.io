# Quarto migration

(NOTE: AI-generated)

## Background

The site was originally built with [Nikola](https://getnikola.com/), a Python-based
static site generator. After several years, the toolchain had accumulated friction:
Python environment management for Nikola itself, Mako templates for any customization,
and a confusing two-branch deploy model (`src` branch = source, `master` branch =
rendered HTML committed directly). This document records the key design decisions made
during the migration to Quarto.

---

## Why Quarto

Quarto was chosen over other options (Hugo, Jekyll, Astro, plain Pandoc) because:

- Native Jupyter notebook rendering — blog posts are mixed `.qmd` and `.ipynb`; Quarto
  handles both first-class with no plugins
- KaTeX math support built-in, globally enabled with one config line
- RSS feed generation for listing pages with no extra plugin
- Category/tag listing pages with filter sidebar out of the box
- The Quarto CLI has a single `quarto render` / `quarto preview` workflow with no Python
  environment to manage separately

---

## Repository layout: `src/` subdirectory

**Decision:** The Quarto project root is `src/`, not the repo root.

**Why:** The repo contains files that are not part of the website
(`decisions/`, `scripts/`, `README.md`, `CLAUDE.md`, `DEVELOPMENT.md`). Putting the
Quarto project at the repo root would require either excluding all those paths from
the render or polluting `_quarto.yml` with an exclusion list. A `src/` subdirectory
keeps website source cleanly separate and lets repo-level docs live at the top level
without any configuration workarounds.

**Build commands use:** `quarto render src/` or `quarto preview src/`.

---

## URL preservation: directory-per-page

**Decision:** Every page is `src/path/to/slug/index.qmd`, not `src/path/to/slug.qmd`.

**Why:** Quarto renders `foo.qmd` → `foo.html`. GitHub Pages serves `/foo` and
`/foo.html` but *not* `/foo/` (with trailing slash). All existing URLs on the Nikola
site used trailing slashes (Nikola's `PRETTY_URLS = True`). To avoid breaking those
URLs the directory form is required: `foo/index.qmd` → `foo/index.html` → URL `/foo/`
works correctly.

---

## Old year-directory posts: keep the nested path

**Decision:** Posts from 2018–2020 that were stored as
`posts/YYYY/MM/DD/slug.md` in Nikola are placed at
`src/blog/YYYY/MM/DD/slug/index.qmd`, preserving the full path.

**Why:** Nikola used the `YYYY/MM/DD/slug` path as the URL for those posts (not
a date-prefixed flat slug). Changing the URL would break links from external sites.
The initial migration incorrectly placed these at `src/blog/slug/index.qmd`
(flat, no date); this was corrected in a follow-up commit once the mismatch was noticed.

---

## `tags:` → `categories:` frontmatter rename

**Decision:** Nikola's `tags:` frontmatter key is renamed to `categories:` in Quarto.

**Why:** Quarto's listing and category-filter features use `categories` as the
canonical frontmatter key. Quarto does not understand `tags` at all — keeping the
old key would silently drop all post tags from the listing filter.

---

## KaTeX enabled globally, no per-post flag

**Decision:** `html-math-method: katex` is set in `_quarto.yml` for all pages.
Posts do not carry a `has_math:` field.

**Why:** Nikola required `has_math: true` on each post to inject the math library.
Quarto's global config removes that per-post overhead. KaTeX loads efficiently
enough that enabling it everywhere has negligible cost. The per-post flag was a
Nikola implementation detail, not a meaningful content signal.

The switch from MathJax to KaTeX was already made in the Nikola version of the site
(see `decisions/math-rendering.md`), so the renderer is unchanged.

---

## `description:` field removed from posts

**Decision:** The initial migration added auto-extracted `description:` fields to
every post; these were subsequently bulk-removed.

**Why:** The auto-extraction (taking text before `<!-- TEASER_END -->`) produced
awkward, truncated descriptions that didn't add value in listings. Quarto's listing
`type: default` shows the beginning of the post body as a teaser when no
`description` is present, which is a better default. New posts written directly in
Quarto can opt in to an explicit `description:` when the auto-teaser is inadequate,
but it is not required.

---

## Blog structure: featured landing page + separate all-posts archive

**Decision:** `/blog/` shows only featured/curated posts. `/blog/all/` shows all
posts with a category filter sidebar and RSS feed.

**Why:** With 70+ posts, a single listing page serving as both the entry point and
the full archive is noisy. The landing page at `/blog/` filters to posts tagged
`_all-time-best`, `_all-time-highlight`, or `_recent-highlight` — a curated
introduction for new visitors. The full archive at `/blog/all/` serves regular
readers who want to browse or filter by category.

RSS subscribers and feed readers are directed to `/blog/all/index.xml` (the feed
generated by the all-posts listing), since that is where all posts appear.

---

## RSS feed at `/rss.xml`

**Decision:** The canonical RSS feed URL remains `/rss.xml` even though Quarto
generates it at `/blog/all/index.xml`.

**Why:** Feed readers and existing subscribers expect `/rss.xml`. Quarto has no
built-in mechanism to rename a generated feed file, and feed readers don't follow
HTML meta-refresh redirects. The `scripts/generate_redirects.py` post-build script
handles this via a file move: after `quarto render`, it moves
`_site/blog/all/index.xml` → `_site/rss.xml`.

---

## All-posts listing: year-prefix glob to avoid self-inclusion

**Decision:** The listing in `src/blog/all/index.qmd` uses the glob
`"../2*/**/index.qmd"` rather than `"../**/index.qmd"`.

**Why:** Quarto auto-excludes the listing file itself from its own listing, but
it does *not* exclude other pages in parent directories. The `../**/index.qmd` glob
matches `../index.qmd` (the blog landing page), which would appear as a post in
the all-posts list. Quarto's `exclude:` config takes frontmatter field matchers
(objects), not path strings, so path-based exclusion is not supported.

The year-prefix `../2*/**/index.qmd` naturally restricts to directories whose name
starts with a digit — which is true for all blog post directories
(`YYYY-MM-DD-slug/`, `YYYY/MM/DD/slug/`) and false for the landing page and any
other non-post pages.

---

## Curation tags kept as regular categories

**Decision:** `_all-time-best`, `_all-time-highlight`, `_recent-highlight` are
stored as regular Quarto `categories:` values, not hidden.

**Why:** Quarto has no concept of hidden tags. The Nikola version hid these
"meta-tags" from the public tag cloud. In Quarto they will appear in the category
filter sidebar on `/blog/all/`. This is an accepted trade-off: the tags are visually
odd but harmless, and hiding them would require either a custom plugin or post-build
HTML surgery.

The featured listing on the blog landing page uses these categories as a filter
(`include: categories: [...]`), so they remain useful.

---

## Redirects via post-build script

**Decision:** Legacy URL redirects (`/links/` → `/resources/`, `/about/` → `/`)
are generated by `scripts/generate_redirects.py`, which runs after `quarto render`.

**Why:** Quarto has no built-in redirect mechanism. The script writes standard
HTML meta-refresh files into the output directory (`_site/links/index.html`,
`_site/about/index.html`). It is hooked as `post-render` in `_quarto.yml` so it
runs automatically during `quarto render`.

---

## `execute: freeze: true` for notebooks

**Decision:** All notebooks use frozen execution (`execute: freeze: true` in
`_quarto.yml`).

**Why:** Re-executing notebooks on every `quarto render` would require all
notebook dependencies (PyTorch, JAX, etc.) to be present in the build environment
and would make renders slow. The source notebooks already contain pre-computed
outputs. Freezing preserves those outputs without re-running the cells.

---

## Footer: social links, no dynamic build date

**Decision:** The page footer contains social links and a static copyright line.
No dynamic "last built on" date is included.

**Why:** Quarto does not process shortcodes in `_quarto.yml` footer values.
Adding a dynamic build date would require either a pre-render script that writes
a `_variables.yml` file and a custom HTML partial, or a post-render find-and-replace
step. For a personal blog this complexity is not worth the benefit — the site
version is visible in the git history if needed.

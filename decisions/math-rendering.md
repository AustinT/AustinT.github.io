# Math rendering

## Problem

`\mathcal` commands (e.g. `$\mathcal{N}$`) rendered correctly in Firefox but showed
a square box in Chrome. The site was using MathJax 2.7.5 loaded via Nikola's built-in
theme template (`math_helper.tmpl`) with the `TeX-AMS-MML_HTMLorMML` config:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
        integrity="sha384-3lJUsx1TJHt7BA4udB5KPnDrlkO8T6J6v/op7ui0BbCjvZ9WqV4Xm6DTP6kQ/iBH"
        crossorigin="anonymous"></script>
```

The `HTMLorMML` output renderer loads font files on demand from the CDN, including a
separate `MathJax_Caligraphic` font for `\mathcal`. Chrome is stricter than Firefox
about loading CDN web fonts, causing that font to silently fail.

## Option A: MathJax 3 with SVG output (explored, not adopted)

The SVG output renderer embeds glyph paths directly into the page HTML rather than
loading web fonts, so it works consistently across all browsers.

Nikola's theme hardcodes the MathJax 2 script URL, so the fix required a site-level
template override at `templates/math_helper.tmpl` that replaces the `math_scripts()`
macro entirely. The override switches to MathJax 3 (`mathjax@3/es5/tex-svg.js`).
MathJax 3 requires the config to be set in `window.MathJax` **before** the script
loads, unlike MathJax 2's `text/x-mathjax-config` blocks.

The template override (Mako syntax, placed at `templates/math_helper.tmpl`):

```mako
<%def name="math_scripts()">
    %if use_katex:
        <script src="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/katex.min.js" integrity="sha384-9Nhn55MVVN0/4OFx7EE5kpFBPsEMZxKTCnA+4fqDmg12eCTqGi6+BB2LjY8brQxJ" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/contrib/auto-render.min.js" integrity="sha384-kWPLUVMOks5AQFrykwIup5lo0m3iMkkHrD0uJ4H5cjeGihAutqP0yW0J6dpFiVkI" crossorigin="anonymous"></script>
        % if katex_auto_render:
            <script>
                renderMathInElement(document.body, { ${katex_auto_render} });
            </script>
        % else:
            <script>
                renderMathInElement(document.body, {
                    delimiters: [
                        {left: "$$", right: "$$", display: true},
                        {left: "\\[", right: "\\]", display: true},
                        {left: "\\begin{equation*}", right: "\\end{equation*}", display: true},
                        {left: "\\(", right: "\\)", display: false}
                    ]
                });
            </script>
        % endif
    %else:
        <script>
        MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']],
                processEscapes: true
            },
            svg: {
                fontCache: 'global',
                displayAlign: 'center'
            }
        };
        </script>
        <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
    %endif
</%def>

<%def name="math_styles()">
    % if use_katex:
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/katex.min.css" integrity="sha384-yFRtMMDnQtDRO8rLpMIKrtPCD5jdktao2TV19YiZYWMDkUR5GQZR/NOVTdquEx1j" crossorigin="anonymous">
    % endif
</%def>

<%def name="math_scripts_ifpost(post)">
    %if post.has_math:
        ${math_scripts()}
    %endif
</%def>

<%def name="math_scripts_ifposts(posts)">
    %if any(post.has_math for post in posts):
        ${math_scripts()}
    %endif
</%def>

<%def name="math_styles_ifpost(post)">
    %if post.has_math:
        ${math_styles()}
    %endif
</%def>

<%def name="math_styles_ifposts(posts)">
    %if any(post.has_math for post in posts):
        ${math_styles()}
    %endif
</%def>
```

**Downsides of SVG output:** math text cannot be selected or copied from the page, and
the visual weight of SVG glyphs differs slightly from the surrounding body text.

## Option B: KaTeX (adopted)

KaTeX is natively supported by Nikola via `USE_KATEX = True` in `conf.py`, requiring no
template override. It renders math as HTML+CSS and loads all its fonts upfront rather
than on demand, which avoids the Chrome font-loading issue. It is also faster than
MathJax.

Config changes in `conf.py`:

```python
MATHJAX_CONFIG = ""  # disabled

USE_KATEX = True

KATEX_AUTO_RENDER = """
delimiters: [
    {left: "$$", right: "$$", display: true},
    {left: "\\\\[", right: "\\\\]", display: true},
    {left: "\\\\begin{equation*}", right: "\\\\end{equation*}", display: true},
    {left: "$", right: "$", display: false},
    {left: "\\\\(", right: "\\\\)", display: false}
]
"""
```

The `KATEX_AUTO_RENDER` block is required to support `$...$` inline math (Nikola's
default KaTeX config only activates `\(...\)` delimiters).

**Known limitation:** KaTeX covers a slightly smaller subset of LaTeX than MathJax.
If a future post needs a command KaTeX doesn't support, Option A (MathJax 3 + SVG)
is the fallback to consider.

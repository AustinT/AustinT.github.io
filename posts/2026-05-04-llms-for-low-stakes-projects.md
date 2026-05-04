---
title: 'Getting value out of coding agents for low-urgency, low-impact projects.'
date: 2026-05-04T12:00Z
tags:
    - using large language models
    - website
has_math: false
---

I've been a somewhat late adopter to coding agents: until ~1 month ago I was
mainly using cursor and asking it to suggest local edits, or occasionally
bigger refactors. In the past 1 month I've been trying to change that. In my
work this has mostly taken the form of giving coding agents bigger open-ended
tasks (e.g. "plan out this big refactor"). However, outside of work I've also
tried just doing _more_ tasks. In this post I'll walk through some use cases
where I used coding agents for low-urgency, low-impact tasks that I'd
previously been procrastinating on. What's impressive is not the task itself,
but how little mental attention completing the task required.

<!-- TEASER_END -->

**NOTE**: all these tasks were accomplished with Claude code, which I chose
simply because I've had a personal subscription to Claude for the past ~1 year.

## Task 1: CV upgrade

A few years ago I created a programmatic CV repo: a bunch of LateX snippets
about individual items that could be combined together into a custom CV by
putting a bunch of `\input` statements in a boilerplate file and setting tags
with the `tagging` package. Unfortunately, it slowly grew into a tangled
mess.[^mess] Since I'm not applying for jobs now I thought the fix wasn't
urgent, so I let it be.

[^mess]: The mess was essentially:
    
    1. Files that were mainly supposed to contain _content_ also contained some formatting,
       so I couldn't really customize the format of any derived CVs.
    2. As I created CVs of different lengths, I added ever more tags into the context files
       (e.g. `phd_short`, `phd_short_no_group_name_bullet_point`, etc), causing them to bloat.
    3. Changes to content for 1 CV spilling over into other CVs (e.g. adding an extra line
       about my work at MSR caused my 1 page CV to expand to 2 pages).

Last week I set Claude code on it. It felt like the perfect task because it
was:

- Low risk (worst case I revert the changes with git)
- Low urgency (I won't need a CV until I apply for another job)
- Safe place for code I don't understand: ultimately the repo is a build script
  for a document, so as long as the document looks good everything is fine
  (there are no "edge cases" to worry about like when you are writing an
  algorithm).

After lots of planning and thinking, Claude recommended migrating to quarto,
which would compile to pdf using typst. The format is simpler than Latex and
there are apparently more CV formats available. It migrated my files, then
wrote a few custom lua scripts to handle the compilation to typst. In the
future I could also put its html output on my website.

Ultimately I was pretty happy with the result. The decision on which backend to
use ultimately took a fair bit of time, so altogether this migration maybe took
~5h of my time. This was probably more than it deserved, but a large part of
this was learning about Claude itself and learning more about quarto (which I
recently learned about in the context of my work anyway).

## Task 2: (not) migrating my wiki to Obsidian

I've kept a wiki for personal notes since the beginning of my PhD. It uses the
[vimwiki](https://github.com/vimwiki/vimwiki) vim plugin. However, I'd heard
good things about [Obsidian](https://obsidian.md/) as an alternative wiki
manager and was interested in exploring it. It is still based on markdown files
stored locally (so I won't be locked into a third party), but apparently has a
lot of other features.

I opened Claude in my wiki and asked it to explore an Obsidian migration.
Ultimately it told me that the experience of editing in vim was likely to be
similar, that the editor might be _worse_ if I normally like vim keybindings,
and it's mainly worth the migration if I plan to use its features like
exploring backlink pages. I concluded that it wasn't worth the switch.

This conversation took ~15m of my time (not counting time when I switch tasks
while claude was thinking). That felt about right for what this task was worth
to me.

## Task 3: fixing math rendering on this website

I noticed an error where `\mathcal` letters on my blog wouldn't render
correctly on Google Chrome. My interim solution was just to not use `\mathcal`
fonts, which is fine because none of my posts are so technical that the
notation and distinction really matters. However, every time I opened my
website repo I saw the item sitting in my uncommitted `TODO.md` file.

I asked Claude about the error, and it suggested migrating to math displayed
with SVG instead. We got it working after 1 failed attempt, and it solved the
issue. However, I wasn't a fan of all the math being images. So I asked it to
think of a different solution, and it suggested rendering math with `KaTeX`.
I'd tried `KaTeX` before but rejected it. I didn't totally remember why but I
had a note last year saying it was rejected. It might have been due to some
math code not rendering properly in a jupyter notebook? In any case, I asked it
to get KaTeX working and it did- probably by fixing whatever config mistake I
made previously.

Overall this took ~20m of my time (spread out over maybe 2h where I was
multi-tasking). Again, this felt about right.

## Task 4: `kern_gp`

In 2024 I wrote a tiny python package for GP inference where the _kernel
matrix_ is the input- allowing you to completely handle the logic of evaluating
the kernel yourself. I called the package `kern_gp`
([link](https://github.com/AustinT/kernel-only-GP/)), and it was used for the
experiments in the paper [Hash Collisions in Molecular Fingerprints: Effects on
Property Prediction and Bayesian
Optimization](https://arxiv.org/abs/2511.17078) which I co-authored last year
with a student, Walter Virany. The package was left as a stub on my GitHub.

I asked Claude to fix up the README, convert the package manager to uv, and
write a GitHub action to publish the package to PyPI, which it did. The package
is now live here:

<https://pypi.org/project/kern-gp/>

Overall this took ~10m only, which felt right.

## Conclusion

Overall it felt really nice to tick a lot of these low-urgency tasks off of my
to-do list. My only complaint is that I can't really multitask between
supervising Claude and doing deep work. The best workflow I have is
multitasking to do several of these tasks at once.


---
title: 'Write research papers to be *skimmed*'
date: 2026-05-04T15:00Z
tags:
    - writing
    - research papers
    - opinion
    - _recent-highlight
has_math: false
---

Don't write your paper for somebody to _read_ it, write for somebody to _skim_
it.

<!-- TEASER_END -->

This is my version of a rule I've heard many times before in different forms.

The justification for this rule is that most papers are very niche, and few
people that will care enough to read every little detail. However, a greater
number of people will want to read the paper at a higher level to understand
the key idea, and an even greater number will just read the title / abstract to
get a "one sentence" version of the paper. Therefore, out of the total number
of hours that readers will spend on your paper, most of those hours will be
spent not fully reading the paper. _This_ is your audience, and you should
write to this audience.

My way of operationalizing this rule is to write for a reader that is
_skimming_ the paper. A reader skimming the paper would appreciate:

- A key figure explaining the method (if possible, this is often hard to do
  well).
- A short introduction which can be read as a standalone summary of the paper.
- Section headers that clearly summarize each section's content.
- Figure/Table captions that are fairly self-contained.
- Important bits of text in bold or italics to catch attention visually.

This is not the only way to operationalize this principle. Another version I've
heard[^heard] is something like "spend equal time on the title, the abstract,
and the main text". It also gets at the truth that most readers won't actually
read the main text, and you should explicitly account for this audience when
writing the paper.

[^heard]: Unfortunately I forget the source: I think it was a podcast?

However, I prefer my version because it feels more actionable. It's focused on
the _product_, not the _time spent_ (which is just a proxy for the state of the
finished product). Titles and abstracts are short, and there is arguably only
so much you can do (both good and bad) for choosing a good title/abstract.
However, the main text of a paper is much longer, and it's really easy to
default into writing a narrative that makes sense end to end but isn't easy to
skim.

Ultimately, regardless of which version of this rule you subscribe to, the
lesson is clear: **write papers for an audience isn't actually going to _read_
the paper.**

---

## PS1: have I followed my own advice?

I think the last 2 papers from my PhD are _ok_: not amazing, but not terrible.

- [Tanimoto Random Features for Scalable Molecular Machine
  Learning](https://arxiv.org/abs/2306.14809) has a short intro and fairly
  clear section headers. The main disadvantage is that the actual algorithm
  isn't described very clearly in the paper.
- [Retro-fallback: retrosynthetic planning in an uncertain
  world](https://arxiv.org/abs/2310.09270) is arguably a bit worse, even though
  I liked this paper better. The sections introduce a bunch of parts of the
  algorithm in different sections before combining them together in §4.2, but I
  don't think this narrative is easy to understand from skimming the section
  titles alone. That being said, we did colour code sections, and the intro is
  fairly succinct.

## PS2: do LLMs change this calculus at all?

Arguably the existence of LLMs to summarize research papers on demand makes the
exact way that papers are written less important. Instead of skimming papers,
researchers can feed it into an LLM and ask for a summary. All things being
equal, I think this makes my advice less important than it used to be.
_However_, I still endorse it, for 2 reasons:

1. Putting a paper into an LLM has non-zero cost (time and money, since tokens
   aren't free). There will be some fraction of your audience that will want to
   skim the paper without asking an LLM (or will skim the paper to _decide_
   whether to give the paper to an LLM).
2. LLM summaries usually don't depart much from the framing of the original
   paper (especially for cheaper LLMs). Clearly framing the important points in
   a way that makes the paper skimmable will probably also result in better
   summaries.


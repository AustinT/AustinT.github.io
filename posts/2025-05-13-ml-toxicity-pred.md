---
title: "Problems with ML for toxicity prediction."
date: 2025-05-13
tags:
    - machine learning
    - medicine
    - chemistry
    - research papers
has_math: false
---

I recently read [a review paper by Seal et
al](https://pubs.acs.org/doi/10.1021/acs.chemrestox.5c00033) about machine
learning for toxicity prediction. Given the length of the paper I thought I
would share my important takeaways. Disclaimer: not everything in this post was
part of the paper, and not everything in the paper is reflected in this post.

<!-- TEASER_END -->

<div class="alert alert-warning">

This post was checked for LLM alpha (see <a
href="/blog/2025-02-24-llm-alpha/">this blog post</a> for details), <i>and does
not have much alpha</i>. Gemini 2.0 flash raised many points given in this post
when I asked it "What are some fundamental problems in machine learning for
toxicity prediction in the context of drug discovery?"

Therefore, view this post as my own attempt to explain the problem and
highlight its importance, but reading this post will probably <i>not</i> be
better than asking an LLM.

</div>

## Context: the "ML person" view of toxicity

Toxicity prediction is often viewed as a classification task where a molecule
is input and classified as "toxic" or "non-toxic". The criticisms raised in
this post are of most significant interest to people who think about toxicity
at this level.

## Problems with "molecules" as inputs

A molecule is just a graph, right? Unfortunately, _no_.

A molecule may have different forms not easily captured by a single molecular
graph.[^everywhere] Two examples:

[^everywhere]: This is an issue for all kinds of cheminformatics tasks, not just toxicity.

1. **Tautomers** are molecules which readily interconvert between each other
   (see image below for examples). One form could be toxic, the other not. A
   single graph cannot represent both forms.
2. **Protonation states** (ie the number of hydrogen atoms bonded to
   oxygens/nitrogens/etc) will change depending on the surrounding pH, changing
   reactivity and charge. Without a corresponding pH input, a molecular graph
   may not represent the actual state of a molecule in the body.

<a title="Example of tautomers. Image by Vaccinationist, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Tautomers.svg"><img width="512" alt="Tautomers" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Tautomers.svg/512px-Tautomers.svg.png?20161224141657"></a>

Essentially, this means that the actual state of a molecule in the body often
_cannot_ be represented by a _single_ graph, and exactly which graph(s) are
most appropriate depends on external conditions like pH. If one wants to use a
single graph as input, there are several incompatible interpretations of what
the question is. Here are 2 that I can think of:

1. If this exact molecule were in the body, would it be toxic?
2. If this molecule were in whatever form(s) it would take under physiological
   conditons, would it be toxic?

The second definition is more compatible with actual experiments (you take the
chemical out of a jar and put it in cells, not observing nanoscopic changes),
while the first would be very useful for _understanding_ toxicity (eg knowing
exactly which form of the molecule is problematic). Unfortunately, "standard
practice" is to not actually answer this question.

## What about dose?

Toxicity of X depends on how much X one is exposed to (the dose). Even water is
toxic at high enough doses. So, asking "is X toxic" without specifying a dose
does not really make sense as a question.

Sadly, toxicity prediction tasks _rarely_ specify doses. In the drug discovery
context this is usually assumed to be a "pharmaceutically appropriate value",
but this of course will also depend on context.

## Endpoints (what is actually measured)

For drug discovery, what ultimately matters is _in vivo_ toxicity in humans.
Since this is expensive to measure (and often unethical), many datasets show
_in vivo_ toxicity in animals or _in vitro_ toxicity to something like
organoids or cultured cells. These endpoints may not match _in vivo_ toxicity
in humans for a variety of reasons:

- Animal biology may not perfectly match human biology
- Cells in a petri dish behave differently to cells in a living body
- The absorption/distribution of a drug can change which cells are exposed to
  the drug and at what concentrations (eg liver cells might get a very high
  dose, brain cells get no dose)

In summary: the labels are not perfect.

## PK / ADME

This slightly overlaps with the previous point, but pharmacokinetics (PK) and
absorption/distribution/metabolism/excretion (ADME) properties of a drug highly
influence toxicity. For example:

- A drug could be toxic if there was prolonged exposure, but it could be
  eliminated from the body very quickly so that toxic effects are not observed
  in practice.
- The opposite could be true: a relatively non-toxic compound could become
  toxic if it is eliminated slowly and accumulates in the body.
- A drug could itself be non-toxic, but could be metabolized (ie reacted) in
  the body to produce a toxic compound

## Summary

"Predict whether this molecule is toxic" is not a well-defined task.

- The exact form of "this molecule" may be unclear
- Toxicity depends on dose, which is not specified
- Most experimental measurements are only _proxies_ for what we really care
  about (toxicity in live humans)
- The way a drug is processed in the body also affect toxicity (which is part
  of what proxy measurements don't capture)

<div class="alert alert-info">

This is a "quickpost": a post which I have tried to write quickly, without very
much editing/polishing. For more details on quickposts, see <a
href="/blog/2025-02-11-lowering-quality/">this blog post</a>.

</div>

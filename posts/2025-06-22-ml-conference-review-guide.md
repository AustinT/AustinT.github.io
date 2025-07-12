---
title: "My review guide for machine learning conference papers."
date: 2025-06-22
tags:
    - machine learning
    - peer review
    - frontpage
has_math: false
---

There is no official step by step guide for how to review ML conference papers
at venues like NeurIPS/ICML/ICLR.[^prev] In this post, I try to explain _my
guide_. It is not official, endorsed, or necessarily good, but I have been
reviewing for 4+ years with this (implicitly) in mind already.

[^prev]: See [my previous blog post](/blog/2025-02-25-no-reviewer-instructions)

<!-- TEASER_END -->

My criteria is essentially:

> accept = correct AND (result OR idea)

Namely, for me to recommend acceptance, the paper must firstly be correct in
every aspect, and must additionally provide something of scientific value. This
"something" is almost always either an idea or a result, and ideally could be
both.

## Elaboration of "correct AND (result OR idea)" criteria

### Correctness

This is essentially "is there _anything_ incorrect with the paper?" Key things
to look out for are:

- Math (mistakes in equations are surprisingly common)
- Incorrect statements about statistical significance[^statsignif] (usually
  "our method did better than all others")
- Incorrect statements of scope (eg claiming "our method is better at
  real-world drug discovery tasks" when only a toy benchmark was used)

[^statsignif]: I have [a blog post](/blog/2025-02-11-peer-review-stat-tests) about this in particular.

**Typos**: note that I _do not_ include typos under correctness. Yes typos are
mistakes, but they are very superficial ones, and peer review is supposed to be
about the _scientific merit_ of the work. I will point out typos if I see them
but I do not consider them when evaluating "correctness".

### Result

Of course, correctness cannot be the only factor, otherwise 8 pages of
statements like "1+1=2" could be a conference paper.

One of the ways that a paper can provide value to the community is by
containing an interesting _result_. This result could be theoretical (eg a
bound or equality), but in ML is most commonly experimental (eg showing the
results of a method or comparing multiple methods).

Beyond simply being correct, an "acceptance-worthy" result should be
interesting, which usually means it advances the field in some way, but could
also simply be contrary to expectations (eg showing that a method works _badly_
when one would otherwise expect it to work well).

### Idea

Another way that a paper can provide value to the community is by containing an
interesting _idea_. Ideas can be:

- An equation (eg an objective function or approximation function)
- A way of evaluating things
- A type of model
- An approximation to something

Almost all papers present an idea of some sort (eg the model they are testing).
When evaluating the idea itself as grounds for acceptance however, the bar
obviously should be higher than simply _having_ an idea. The idea should be
novel, relevant to the community, and non-trivial. Beyond that it is hard to
describe what an "acceptance-worthy idea" is. 

One way to describe it is whether I think "oohh, that's a good idea" while
reading the paper. I don't think this when reading most papers.

Another way to describe it is that I generally don't consider ideas of the form
"what if we did X" to be good ideas. If that's your idea, then do X and show
the result.

In contrast, a type of idea that I usually _do_ consider worthy of acceptance
is "here is an equation which captures the goal Y". If I think Y is an
important goal but hard to precisely define mathematically (eg fairness), and a
paper proposes a reasonable definition, I think that is an important
contribution by itself!

## How does this criteria differ from that of other reviewers?

With the obvious caveat that every reviewer is different, I see the biggest
differences as:

- Correctness being non-negotiable: often in reviewer discussions I have raised
  a serious error in the paper, and other reviewers do not see this as a
  sufficient reason to withhold their acceptance recommendation.
- Willingness to accept a paper without a "result": in principle I see no issue
  with accepting a paper that introduces an idea but does not implement/test
  it. It seems like relatively few reviewers are able to do this. Of course,
  the idea must be very good for me to recommend acceptance based on the idea
  alone!
- No attitude of "reject based on mistakes". It is very common for reviewers to
  focus on a weak section and use that as a justification for rejection (eg
  "theoretical justification was weak, reject"). However, I try to ask myself
  about the paper's merit _excluding_ bad sections. Sometimes I will recommend
  acceptance based on other parts of the paper and simply ask the authors to
  remove a problematic part.

## Some examples

Without giving too much away about past papers I have reviewed, here are some
examples of how I have applied this criteria in the past:

- Dataset paper which evaluates many methods on a new dataset, _but_ the
  dataset was constructed in a nonsense way. I recommended rejection on the
  basis of correctness, even though the paper was well-motivated and clearly
  put a lot of effort into the evaluation.
- Bayesian optimization paper which proposed a new acquisition function but
  only did a small number of toy experiments: I recommended acceptance because
  I thought the idea was interesting. I thought the idea was worth testing on
  real-world problems and I was ok that the authors did not do that (benchmarks
  in BO can be bad).
- A complicated and poorly explained method which performs marginally better on
  molecular property prediction benchmarks:[^every] typically I recommend
  reject because there is no discussion about statistical significance (so I am
  not convinced by the result), nor am I convinced by the idea (because the
  idea seems to be "we tried a bunch of stuff and saw what gave the highest
  number").
- Paper proposing a sensible method but with a nonsense theoretical
  justification: despite doing ok at the task the authors set out to solve, the
  paper contained a theory section with a serious error, so I recommended
  rejection despite the empirical results.

[^every]: This has actually been ~25% of _all_ papers I've ever reviewed 😅

## What does my actual reviewing process look like?

This post has mostly described my reviewing _criteria_, not how I actually go
about reviewing papers. That is actually fairly standard and uninteresting. My
process is:

1. Read the paper end to end, make notes of what the paper's "ideas" and
   "results" are, and anything to check for correctness.
2. Go back and check correctness of anything that seemed suspect.
3. Evaluate the merit of the idea and results. Are one of these enough to merit
   acceptance independently? What about together?
4. Write the review text saying more or less what I think the paper's value is.

## Conclusion

In this post I explained my "accept = correct AND (result OR idea)" approach to
reviewing ML conference papers, and how this [differs from what I view as the
mainstream
approach.](#how-does-this-criteria-differ-from-that-of-other-reviewers) If
you've made it to the end of this post you might still think that the review
criteria I explain here are not precise enough to be a "guide". That's fair: I
discovered when writing this that it is actually very difficult to write a
complete "guide" that walks one through the reviewing process. That being said,
I think my criteria turns reviewing into a series of checks: you can check for
correctness, you can check for the validity/significance of the paper's
idea(s), and you can check validity/significance of the paper's results.
Hopefully that helps! If you agree / disagree with anything I wrote here, feel
free to contact me!

---

<div class="alert alert-info">
This is a "quickpost": a post which I have tried to write quickly, without very much editing/polishing.
For more details on quickposts, see
<a href="/blog/2025-02-11-lowering-quality/">this blog post</a>.

I have actually intended to publish a more polished review guide for around 4 months,
but decided that it is taking too long and that I should just write a slightly less polished version
but publish it sooner.
</div>

<div class="alert alert-success">

This post was checked for LLM alpha (see <a
href="/blog/2025-02-24-llm-alpha/">this blog post</a> for details). 
I asked
Claude 3.7 Sonnet
and didn't get back my simple rule,
so I think publishing it has some value.
Part of that value is promoting this idea
rather than introducing it as novel.
</div>

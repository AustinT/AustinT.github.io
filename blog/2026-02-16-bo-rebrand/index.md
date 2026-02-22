---
title: 'Rebranding BO away from "black-box" and towards "model-based"'
date: 2026-02-16T15:00Z
tags:
    - machine learning
    - bayesian optimization
    - opinion
    - _recent-highlight
has_math: false
---

In a recent blog post ([link](/blog/2026-01-25-model-centric-bo/)) I described
my "model-centric" view of Bayesian optimization (BO), essentially arguing that
the model is the most important component of BO and BO users (and researchers)
should do more to get it right. Under the assumption that the reader broadly
agrees with the content of that post (or at least thinks this view of BO is one
of several valid views), here I want to argue that the BO community should
_re-brand_ itself more towards model-based optimization and away from black-box
optimization.

<!-- TEASER_END -->

## What is a "rebrand"?

BO is not a company or specific product, and therefore does not _officially_
have any kind of brand. However, most BO papers and textbooks mention similar
points in their introductions and descriptions of BO: black-box functions, use
of uncertainty, exploration-exploitation trade-off, Bayesian models (especially
Gaussian processes). Since papers and textbooks are some of the primary ways
that people learn about BO, collectively I think they do form a kind of
"brand". If I were to describe this brand as an elevator pitch of a company,
I'd say:

> You give us an expensive black-box function, we will efficiently optimize it
> using a Gaussian process surrogate model that precisely balances exploration
> and exploitation.

I bet most BO researchers wouldn't fully agree with this statement. However,
from talking with a lot of non-BO experts at conferences, this is how I think
the typical person in ML would describe the value proposition of BO.

Therefore, in my opinion a "re-brand" is changing this brand: doing something
to make the typical BO user or ML researcher view BO differently. Most likely
this "something" will be describing BO differently in papers, but I'll come
back to "how" to do the rebrand later. Let's first focus on what.

## What brand _should_ BO have?

My elevator pitch for BO's value proposition would be:

> You give us a function and your model of the function, we turn this model
> into an interpretable sequential decision algorithm tailored to the
> constraints and trade-offs of your particular problem.

Compared to the current brand, this emphasizes:

- Model as an _input_.
- The value add being producing a decision algorithm _from_ the model.
- Customization of the algorithm for particular constraints and trade-offs. 

It _deemphasizes_:

- Black-box nature of the function (still true, but BO is not exclusively black
  box).
- Uncertainty (this comes in naturally as part of the model).
- Exploration/exploitation (I think this is one of many trade-offs you can
  customize).

## _Why_ should it have this brand?

It's 2026 and everybody's attention is focused on the amazing advances of LLMs
and agents. Implicitly everybody is asking the questions

1. Should I use an LLM agent to do this task?
2. Should I replace my existing solution with an LLM agent?

I don't believe BO is obsolete, but there are parts of BO which don't work well
and I believe can be augmented or replaced by LLMs. Essentially my suggested
rebrand is to emphasize the use cases where I think BO will be most relevant
(ie not replaced by LLMs) in the next 5-10 years.

Let's start by focusing on the positives of LLMs and how they might disrupt BO.
First, LLMs are amazing at multi-modality, meaning that any black box
optimization problem whose inputs/outputs can be represented as tokens can
easily be fed to an LLM. BO used to stand out by making fewer assumptions than
other optimization algorithms (eg not requiring gradients). Unfortunately, I
think BO can no longer compete on "breadth": LLMs are the clear winner here.
LLMs are also clearly _easier_ to use than BO (at least on small datasets): you
can put all data into the LLM's context window, describe the problem, and ask
for a decision. BO is difficult to set up and I don't see that changing.
Clearly BO's value needs to come from other areas (eg "quality" or
"reliability").

Intuitively I would expect BO to perform better than LLMs, but there are many
situations where LLMs will probably perform better. Especially on problems with
tiny amounts of data (eg < 10 data points), I bet LLMs might actually be
better-calibrated surrogate models than GPs. A short textual description of
what the output variable actually is means the LLMs can leverage pre-training
knowledge to suggest values within a reasonable range, and some basic knowledge
about what influences a property. For example, LLMs probably won't suggest a
house price of $1, a binding affinity of -100 kcal/mol, or a learning rate of
`1e-10`. The same isn't true for GPs: on small datasets the learned mean and
outputscale can be severely misspecified.

LLMs can also capture user preferences much more easily than standard BO. BO
algorithms are controlled by a bunch of semi-interpretable hyperparameters,
tuning of which is often more of an art than a science. LLMs can be given
specific behavioural instructions in text form. You can tell the LLM to
"explore" or "exploit" more directly, whereas in BO this is indirectly
controlled by a bunch of hyperparameters. Ultimately I expect BO to make better
long horizon decisions than LLMs (since its explore/exploit trade-off is
governed by theory and LLMs have limited context lengths), but over short
horizons LLMs might actually be better.

That being said, a huge _disadvantage_ for LLMs is their lack of
interpretability (which is even worse for closed-weight models). Although the
outputs usually seem reasonable, they can be completely "hallucinated" and
appear for the wrong reasons. Reasoning models and RAG models are in some ways
attempts to work around this and ground LLM responses in something more
concrete, but as far as I am aware there is still evidence that they can be
"gamed": models can output an answer that does not match the reasoning trace,
and they can also ignore context retrieved as part of a RAG process. This means
LLM-based systems might _appear_ to be following user instructions closely,
while actually not following them at all.

In contrast, basically all versions of BO _guarantee_ that the decision will be
supported by the outputs of the surrogate model.  This is how I believe BO will
continue to provide value into the future. For applications where one has a
trusted predictive model and wants to use it to make decisions in a precise
way, LLMs introduce uncertainty and unpredictability, while BO can be set up to
behave exactly as implied by the predictive model.

Therefore, it feels appropriate for me for BO's "brand" to align more closely
to this core value proposition (unlike the current black-box brand which
obscures this advantage).

## Why think about this _now_?

The strength of the BO research community depends on people outside the
community seeing value in BO. Most BO research is supported by government
research grants or tech companies supporting an in-house BO team. A strong
value proposition helps convince these people to keep funding and supporting
research in this area.

BO has not yet been "eaten" by LLMs. But it is possible that LLMs might be able
to do as well as BO on standard black-box benchmarks within a couple of years.
If this happens, funders who previously funded BO research because they
expected it to yield efficient general-purpose black-box optimizers may start
to lose faith that this is the correct approach. That might inevitably force
the BO community to adopt a different "brand", at least in grants and internal
presentations. My argument is simply that it would be better to do this
_proactively_. Rebranding takes time, and emphasizing a different value
proposition _after_ the research has been perceived as "not the right approach"
might come across as opportunistic and dishonest.

Even if the scenario above (LLMs beating BO at black-box optimization
benchmarks) does _not_ occur, I still don't think much is lost from doing this
kind of rebrand. The key points are arguably still true, and the new branding
does not in any way _deny_ BO's effectiveness as a black-box optimizer (just as
the current branding does not deny BO's effectiveness at turning models into
decision algorithms).

## How would the "rebrand" actually be done?

I don't have a complete answer to this, but the BO community is small, so I bet
a lot of changes could be achieved if BO researchers:

1. Described BO in a different way in their papers and open source software.
2. Wrote BO software to be more accommodating of custom models.
3. Clearly articulated this benefit of BO (perhaps via blogs like this one).

## Summary

In this post I explained why I think BO has the brand "black-box optimizer" as
a result of its description across many papers, why I'd prefer a brand more
like "turn models into decision algorithms", why I think this is more aligned
with BO's long-term value proposition over LLMs, and why we should do this
proactively by describing BO differently _now_.

If you disagree with my argument, I encourage you to reflect on what you think
BO's brand _should_ be. Arguably the current brand was not an intentional
choice, and may not line up perfectly with how you see BO's value. At the very
least, I think we should try to describe methods in a way that emphasizes their
strengths and what problems they are suitable for, rather than just describe
methods in the same way as all previous papers!


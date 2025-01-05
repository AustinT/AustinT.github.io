---
title: "Scientific conferences as approximate Bayesian inference"
date: 2024-11-17
tags:
    - speculation
has_math: true
---

Scientists should ideally form their beliefs based on evidence and update their
beliefs as new evidence arrives. Unfortunately, humans are far from perfect
Bayesian thinkers and therefore may struggle to do this properly. In this post
I explain how conferences help scientists perform better Bayesian inference.

<!-- TEASER_END -->

## Basic model of the perfect Bayesian scientist (PBS)

Let $x$ be a potential fact about the world like "Amyloid plaques cause
Alzheimer's disease",[^1] and $y_1,\ldots,y_N$ denote individual observations
from scientific studies, such as "in a study of X Alzheimer's patients in
hospital Y, amyloid plaques were observed in Z patients". A PBS would have a
prior $p(x)$ about the validity of $x$, and a model $p(y_1,\ldots,y_N|x)$ of
how likely different observations are for all possible values of $x$. They
would hold probabilistic, data-driven beliefs given by the posterior
distribution

$$p(x|y_1,\ldots,y_N) \propto p(x) p(y_1,\ldots,y_N|x)\ .$$

[^1]: This is just an example topic: I'm not a biologist and this is definitely not something that I have an informed opinion on.

## How do conferences help?

Real scientists are very different than PBSs, and generally perform sub-optimal
belief updates. Several factors of conferences can make these updates less
sub-optimal.

### Factor 1: batch update instead of sequential update

For a PBS, it should not matter whether they observe $y_1,\ldots,y_N$
simultaneously or one by one in an arbitrary order: their resulting posterior
will be the same. Real humans do not work this way. If data points are observed
one at a time, unless people make an explicit effort to track or count things,
it is very easy to over or under update based on a single observation.[^2]

[^2]: If this doesn't intuitively seem true to you, a useful intuition pump is to imagine estimating $P(\mathrm{heads})$ for a (potentially) biased coin. If $N=1000$ observations are made simultaneously, people will probably update their beliefs to closely match the empirical distribution of heads. If instead people see 1 observation per day for 1000 days, they probably won't arrive at the same estimate unless they explicitly track outcomes.

Conferences present a lot of research simultaneously, instead of the constant
trickle in scientists' day-to-day lives. This probably allows for a belief
update closer to that of a PBS.

### Factor 2: lower selection bias

There is far too much literature for scientists to actually read everything,
and many scientists will choose a reading list from a _biased_ source (eg
papers from specific scientists). This could result in a belief update which
ignores a lot of evidence in a non-random way: for example, reading only about
amyloid plaques may leave one unaware of possible alternative causes for
Alzheimer's. Sufficiently large/diverse conferences will expose scientists to a
less biased pool of evidence, thereby potentially allowing for a less biased
update.

Mathematically, this is equivalent to

$$\tilde p(x|y_1,\ldots,y_N)\propto p(x) p(y_{i_1},\ldots,y_{i_k}|x)$$

being a better approximation when $i_1,\ldots,i_k$ are sampled independently
instead of non-independently.[^3]

[^3]: Both are arguably bad approximations though.

### Factor 3: updates for distributed inference across scientists

Even if conferences present a less biased selection of the available evidence,
individual scientists can still only read a small fraction of all papers.
Conferences provide a good venue for scientists to directly update their
beliefs based on the beliefs of other scientists. If those other scientists
have read a different subset of papers, this is essentially the same as
_distributed_ Bayesian inference (where different "workers" see different
subsets of the data).

## Conclusions

For me, thinking about conferences as a form of Bayesian updating suggests:

1. Conferences are most worth attending when attended by people outside your
   usual "niche" as a scientist (factor 2)
2. Bigger conferences will be more useful than smaller ones (factor 1)
3. Talking to people who work in different sub-fields will help gain
   perspective (factor 3)

Of course, there are reasons to attend a conference besides forming accurate
beliefs, such as finding collaborators, getting a job, or learning more about a
specific topic. For these goals, the opposite advice might apply (small focused
conferences could be better).

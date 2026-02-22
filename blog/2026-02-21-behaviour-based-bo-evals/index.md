---
title: 'Behaviour-based evaluations in Bayesian optimization'
date: 2026-02-21T22:00Z
tags:
    - machine learning
    - bayesian optimization
    - opinion
    - _recent-highlight
has_math: false
---

I think the Bayesian optimization (BO) research community needs to change its
evaluation practices. In a [previous post](/blog/2026-01-25-model-centric-bo/)
I explained how I think users should generally bring their own model to BO and
try to calibrate it to their beliefs/expectations. In _this_ post, I explain
why existing evaluation practices are not well-suited to this stance on BO, and
outline a different approach to BO evaluation based on algorithm behaviour.

<!-- TEASER_END -->

**Disclaimer**: this post is written under the assumption that the reader
broadly agrees with the arguments in my [model-centric
BO](/blog/2026-01-25-model-centric-bo/), [not caring about toy BO
benchmarks](/blog/2026-02-08-bo-benchmarks/), and [BO
rebrand](/blog/2026-02-16-bo-rebrand/) posts. If you don't agree with the
arguments from these posts, you might still find these evaluation ideas
interesting, but maybe less compelling.

## What are current BO evaluation practices and why are they problematic?

Broadly speaking, most BO papers use a _regret_-based evaluation. For
theoretical works this is basically the only kind of evaluation practiced, and
for empirical works the common practice is to plot either the best y value over
time (linearly related to simple regret) or the cumulative sum y values over
time (linearly related to cumulative regret). Especially in empirical works,
the core claim for a method's efficacy is typically comparing regret values of
their method and other methods.

Of course, users probably don't care about the exact benchmark problems studied
in the paper, they care about their _particular_ problem, and therefore the
benchmark results are useful only insofar as their conclusions transfer to the
user's particular problem. There are many reasons to believe this might not
hold, even in the "ideal" case where users run the exact algorithm from the
paper on their own problem (see my [post about toy BO
benchmarks](/blog/2026-02-08-bo-benchmarks/) for more on this). However, if we
expect that the user won't use the same model as the paper, I am _especially_
doubtful that performance claims from benchmarks will apply in this setting.

A lot of this is because the mainstream regret-based evaluation framework makes
does not provide insight for _why_ certain methods achieve better regret than
others, especially in the non-asymptotic setting where few theoretical results
apply. A lot of different qualitative behaviours could potentially yield
similar regret values. For example:

1. The method "intentionally" exploits the region around the training data and
   finds a local optimum.
2. The method "intentionally" explores regions far from the training data and
   "gets lucky" by finding a good point.
3. The method "intends" to explore OOD, but is underconfident and has huge
   uncertainty values very close to the training data. Therefore, in practice
   it basically exploits the region around the training data and gets similar
   results for scenario 1.
4. The method "intends" to exploit locally, but is extremely overconfident in
   its predictions and ends up selecting points very far from the training
   data. It gets lucky and finds a similar point as in scenario 2.

(**NOTE:** when I use the word "intention" here I mean "an algorithm design
decision made with a particular behaviour in mind", for example trust-region BO
limiting queries to a small region or UCB exploring points which _might_ have a
high objective value. I acknowledge this is a subjective area)

It is intuitive to me that in each of these scenarios, changing the model would
likely have a very different effect on regret performance. Therefore, I believe
that studying the regret only will be insufficient to predict algorithm
behaviour with new models. Therefore, to the extent that one does machine
learning experiments in order to give guidance to _users_ of algorithms, I
believe something more than regret is needed.

## From regret to behaviour

I think the sensible alternative to regret is _behaviour_: studying the
algorithm in x space instead of y space. Seeing which points x it selects (and
why it queries those points) is likely much more informative than looking at
regret plots. It's like seeing the full solution to a math problem instead of
just the final answer. Unfortunately, outside of 1D benchmarks where the entire
function and data can be nicely plotted, this is usually not easy to visualize,
and even harder to distill into a single number or metric. It's not an easy
thing to turn into a "benchmark".

I think that's ok. Benchmarks are much more suited to _confirmatory_ studies
that aim to answer a specific question. _Exploratory_ questions like "how does
this algorithm behave" are also valid targets for scientific study, even if
there is no statistical test at the end or firm conclusion!

## Ideas for how to evaluate behaviour

I haven't settled on a single recipe or answer for evaluating behaviour of BO
algorithms, but here are some approaches I find informative and interesting.

### Different decisions at a single iteration

Most BO algorithms are _stateless_: the only thing carried forward between
iterations is the surrogate model itself, which could in principle just be
refit from scratch on the data available. Therefore it is possible to
initialize BO at an arbitrary starting point in the optimization and see what
decision it makes.

This is a powerful tool to compare algorithms (and models) side by side. One
can fit a single surrogate model to some starting data, then apply 2 different
acquisition function + optimizer pairs (the remaining 2 parts of any BO
algorithm) and see which different points they choose. If they choose different
points, you can look at the model predictions to understand why. Usually it
will be because the acquisition function values are different, and from this
you can understand preferences of each acquisition function (eg UCB often
preferring higher uncertainty than EI). Occasionally you will find an error
with acquisition function optimization (eg the same point x maximizes both
acquisition functions, but one of the acquisition function optimizers failed to
find x).

Alternatively, you can compare 2 different models using the same acquisition
function + optimizer and see how the decisions differ. In this case,
differences in behaviour should come purely from the models' different
predictions, and you can understand how modelling decisions lead to behaviour
decisions.

It may seem unintuitive to look at a single decision in BO, because it is an
algorithm usually run over many iterations. But, differences in long-run
behaviour ultimately stem from different decisions being made at individual
steps, and examining when algorithms make different decisions can form the
basis for understanding differences in long-run behaviour.

### Counterfactuals at a single iteration

When evaluating single decisions you can also ask questions like "what would
the predictions need to be for a specific point x to be chosen"? For example,
in toy problems where the global optimum is known, you can ask "what
predictions would need to be made at the optimum for it to be chosen right
now?" This might provide helpful modelling information, at least for those
particular problems. You can also ask questions like "what would predictions
need to be for the model to choose a point far away from the training data" or
"how would the decision change if one of the surrogate model parameters was
perturbed by a small amount?" This can be incredibly useful for deriving
failure modes of optimization.

### Restricted decision set, multiple iterations

Instead of optimizing over a large space X, you can restrict the algorithm to a
finite set of options x1, x2, etc and maximize the acquisition function by
brute force over the set. This technique obviously can't be used to evaluate
acquisition function optimizers (since it is replaced by brute force), but can
be used to compare models and acquisition functions. This kind of study helps
you understand how algorithms will behave on a smaller set of "representative"
options.

For example, you could have:

- 2 "sensible" points far from the training data
- 2 "nonsensical" points (eg a non-physical molecule or all-noise image)
- 2 "good" points close to training data
- 2 "bad" points close to training data

You can run BO for ~4 iterations and track for each algorithm which 4 choices
it makes. If an algorithm chooses "nonsense, nonsense, bad, bad" probably
something is wrong. If an algorithm makes sensible choices you can see what the
acquisition function difference was between good and bad choices (ideally it is
large).

If the decision set is slightly larger you can look at statistics like "what
fraction of inputs were chosen in common" and "what are the statistics of
points chosen by BO algorithm A but not by algorithm B?" 

### Algorithm "switches"

Run BO algorithm A for N iterations, then use its evaluation trajectory to
initialize algorithm B and run for M iterations. Compare with running algorithm
A and B for (N+M) iterations. Significant differences in performance can build
understanding for what's happening in the algorithm without needing to examine
the entire long trajectory in a lot of detail. Some examples:

- If A > A/B hybrid > B, probably algorithm A is just better than B on this
  problem.
- If A/B hybrid > A > B, this is interesting. One possible explanation: A is
  exploratory, B is exploitative. A explores a lot, finds better solutions, but
  doesn't exploit enough. B doesn't explore enough (and this is a losing
  strategy if the initial training data is in a bad region of x space). A/B
  hybrid will explore then exploit.
- If A > B > A/B hybrid, this is also interesting. One possible explanation is
  that the algorithms explore in different ways (eg in different subspaces).
  Individually they perform ok because they explore/exploit within their
  subspace, but combined together they just explore too much (and never exploit
  the areas they've explored).

## Summary

In this post I argued that if we assume users will generally use a custom model
in BO, then trends / findings from regret-based analysis are unlikely to remain
true because similar regrets can be achieved by hugely different behaviours. I
suggested studying algorithm _behaviours_ instead, even though this is harder
to quantify. I gave some ideas for how "behaviour" could be turned into simpler
questions with clearer answers (although not ones that could easily become a
"benchmark").

This is one of the things I'd like to see most in academic BO papers. I find it
disappointing to read papers' experiment sections and walk away with little to
no understanding for what kind of decisions the model is actually making (it
feels like reading LLM papers without ever seeing examples of its output text).
If you are doing academic BO research, I'd love to hear from you about these
ideas. Please feel free to reach out!

---

## (Bonus) Could these evaluation settings be turned into a benchmark?

Maybe. I could imagine something like a set of challenging "decision scenarios"
(aka BO initializations) with a desired decision in each one. BO algorithms
could be run for a single iteration in each case, and the fraction of scenarios
where the "right" decision is made could be reported as a metric. However, I
imagine that defining a "right" decision in each scenario is difficult because
it is inherently subjective. Furthermore, it would be hard to capture long-term
explore/exploit trade-offs here (a BO algorithm's exploratory decisions early
on will put it in a fundamentally different scenario than an exploitative
algorithm).


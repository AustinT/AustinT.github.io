---
title: "Reaction model scores are CRITICAL to multi-step retrosynthesis."
date: 2025-01-26
tags:
    - retrosynthesis
    - machine learning
    - speculation
has_math: false
---

Machine-learning for retrosynthesis is a popular research topic. Popular
sub-topics include:

<!-- TEASER_END -->

- **New models** to output plausible reactant sets for a given product
  (innovations are generally architecture, sometimes training data).
- **New search algorithms** to chain together reactions to form a synthesis
  route.
- **New heuristics** to guide algorithms (eg learning a value function).

(For context, most of my work in this area has been on search algorithms.)

In contrast, assigning _scores_ to reactions (which I will call _"reaction
scores"_ for the remainder of this post) is relatively unpopular, or at the
very least is typically treated as an implementation detail in most papers. **I
think this is a mistake**. From a mixture of talking to experts and playing
with these algorithms myself, I've come to the opinion that reaction scores are
among the _most important_ factors in retrosynthesis. In the remainder of this
post I will try to explain why this is. If somebody finds my arguments
compelling and wants to turn this into a proper research paper, please
do![^post]

[^post]: This is actually part of the reason I am writing this post. If you do extend these ideas into a paper, I would appreciate being mentioned in the acknowledgements of your paper (perhaps linking to this post), but of course I have no claim or expectation to be a co-author on any such work if all I contribute is a seed idea. Please, go forth and research!

## What are reaction scores?

Essentially just a number assigned to a reaction. Common choices are:

- Logit or softmax value of a template (for template-based models)
- Likelihoods (for autoregressive models like transformers on reaction strings)

Not all models have them, but most do. In `syntheseus`[^syntheseus] (which I
helped write), most of the default models produce a score.

[^syntheseus]: <https://github.com/microsoft/syntheseus/>

## How are scores used by search algorithms?

The most common multi-step search algorithms all have a "slot" for a reaction
score. In retro\* (essentially just A\*), each reaction has a
cost.[^scoresvscost] Costs are added together to produce a route cost. In MCTS,
reaction scores can be used as "prior" values to weight the upper confidence
bound, and delay exploration of low-scoring reactions. Thus, in addition to a
_"search heuristic"_ like rollouts or learned "value functions", these reaction
scores significantly influence the behaviour of search algorithms.

[^scoresvscost]: Scores (where higher is better) are usually transformed into costs (where lower is better) with a simple transform, eg -log().

## How much do scores influence search behaviour?

Short answer: very much.

Longer answer: it slightly depends on the algorithm, but generally a lot. In
retro\*, if the reaction costs are set to a constant value, the cost of a
synthesis route essentially becomes its length. Retro\* will begin to behave
like breadth-first search (and if a 0 heuristic is used called retro\*-0 in the
original paper, it will almost[^retrostar0caveat] exactly be breadth-first
search). For MCTS, more uniform scores will also encourage more uniform
exploration (although the exact balance also depends on the setting of its
exploration constant).

[^retrostar0caveat]: "Almost" here is because 1) there is random tie-breaking and 2) for convergent synthesis routes whose total number of reactions is not just its length, it may make slightly different choices. These will only be important however after _every_ reaction which produces the target has been explored, which may take a long amount of time.

It goes even deeper. Consider not _uniform_ (aka _uninformative_) scores, but
_adversarial_ scores, ie ones where the reactions in the "best" route are given
low scores. It should be easy to convince yourself that an algorithm can
essentially be forbidden to explore a desired reaction if the score is set to
be low enough (aka cost is high enough). So, the fact that algorithms are
generally able to find reasonable synthesis routes essentially _requires_ that
reaction scores are at least not _terribly_ misleading.

It goes even deeper. How do single-step reaction models "choose" which
reactions to output and which reactions not to output? For example,
template-based models generally assign a score to _every_ template in the
library. Why are typically only ≤100 returned? Often, this is because reaction
scores are used to _pre-filter_ reactions, deciding which reactions will even
be _considered_ by a search algorithm and which reactions _won't_, strictly
limiting the possible routes that can be found. Remember: a low-scoring
reaction may be explored by a search algorithm if it is run for long enough
(although this may still be impractically long), but a reaction not in the
search graph can _never_ be explored.

## Is this a problem?

Short answer: unclear

Longer answer: the fact that retrosynthesis algorithms tend to work well in
practice suggests that scores output by retrosynthesis models are generally
reasonable, at least on the kinds of tasks which are usually benchmarked. This
must be due to a combination of:

1. The training reactions for single-step models overlap heavily with the kinds
   of reactions which are desired for multi-step search.
2. Single step models learn some kind of _generalizable principles_ for which
   reactions to score highly.

Maybe there isn't too much of a need to improve reaction scoring. However, one
scenario where I could imagine a significant difference is synthesis planning
settings with a highly-constrained set of building block molecules (aka
purchasable molecules). Here, many reactions which _normally_ lead to synthesis
routes may not be feasible. If reaction scores are unchanged, algorithms may
spend a long time searching in branches which rely on building blocks that are
normally present. Adjusting the reaction scores might be required.

## Conclusion

People working on retrosynthesis should at least acknowledge that reaction
scores have a huge impact on algorithm behaviour. Although "default" scores
seem to work reasonably well, this may not always be the case. I think this
topic deserves more explicit attention than it receives currently.


---
title: "We are underselling the modularity of Bayesian optimization"
date: 2026-02-09T00:00Z
tags:
    - machine learning
    - bayesian optimization
    - opinion
    - _recent-highlight
has_math: false
---

I think the Bayesian optimization (BO) community is vastly underselling one of
BO's most practically appealing features: _modularity_. A "modular" algorithm
is one composed of individual parts which are largely exchangeable. I think BO
is extremely modular, and this is something users want in practice, but BO
papers rarely describe it in this way. This post outlines these points in more
detail and ends with some recommendations.

<!-- TEASER_END -->

## BO is modular

I think BO algorithms can be broken into three modules which are largely
independent.

1. The surrogate model
2. The acquisition function
3. The optimizer of the acquisition function

I bet ~75% of BO researchers would immediately agree with this. The remaining
researchers would probably raise objections like "expected improvement (EI) has
an analytical form for GP models but not Bayesian neural networks, isn't that a
violation"? So, let me be precise about what I mean by "independent": I mean
that their _goals_ are different and that they are _conceptually orthogonal_.

Let's use GPs/EI as an example that might "feel" like non-independent choices.
Let's first consider the _goals_ of the surrogate model and acquisition
function. I believe the goal of a BO surrogate model is specifying a set of
probabilistic beliefs about the objective function in the most accurate way
possible (I expect most BO researchers would agree). Choices of surrogate model
should largely be determined by the question "what do I believe about f?"
Conversely, I believe the goal of the acquisition function is to specify a
desired algorithm behaviour given a set of beliefs (and again, I expect most BO
researchers would agree). Choices of acquisition function should be determined
by the question "how do I want the algorithm to behave?"

I see no particular reason to expect strong correlations between beliefs and
desired behaviours across problems. Why should the belief that all joint
distributions on outputs are Gaussian (the fundamental assumption of a GP)
compel you to want the algorithm to always myopically aim for maximum
improvement on the best point seen so far (the EI acquisition function)? I see
these as completely _conceptually orthogonal._

Of course, EI being available in closed form is absolutely an advantage of
using the GP+EI combo. However, I'd much rather call that a _synergy_: a
_benefit_ derived from using a particular combination, rather than a
fundamental _dependence_. I think the difference is that a synergy is really a
matter of convenience, while a true dependence implies that some choices are
intrinsically better together than others.

Let me explain the difference between these two with an analogy. I often get a
burrito on my way home from work because there is an ok burrito place on my
walk from Recursion's London office to King's Cross station. I would describe
this as a _synergy_ between food and travel destination (ie this particular
combination saves time), but would argue that overall the food you eat is
independent of one's travel destination (eg burritos are not intrinsically
suited to going home). Food choice and destinations have different goals and
are conceptually orthogonal.

In this post, I am not denying the existence of synergies in BO- they
absolutely exist. My point is that synergies do not contradict modularity:
certain combinations being easier does not mean that substitutions cannot be
made, just that there will be difficulties in doing so.

With this clarification, I'll proceed as if the reader accepts the claim that
BO _is_ intrinsically modular.

## Why is modularity desirable?

Modularity is useful for many reasons:

- **Debugging**: if different modules are "responsible" for different
  functions/features of an algorithm, a bug (or other undesirable behaviour)
  can be localized to a particular part of the algorithm.
- **Corrigibility**: if the algorithm is not doing what you want, you can
  substitute a module to change its behaviour in a somewhat predictable way.
  For example, since BO's behaviour is controlled by its acquisition function,
  you can be confident that increasing UCB's beta coefficient should increase
  exploration for all model types.
- **Reuse**: deploying an algorithm in a new setting doesn't require inventing
  a completely new algorithm since some parts could be re-used. For example, BO
  on a completely new data type (eg infinite sequences) might require a new
  model (eg a GP with a new kernel) and a new acquisition function optimizer
  that works in infinite sequence space, but acquisition functions like EI or
  UCB could still be used (and you know how they will behave roughly).

Practitioners encounter these challenges all the time, and they are some of the
biggest pain points of "black box" algorithms. For example, there are many
optimization algorithms of the flavour "train a generative model somehow, then
sample from it as your policy." If you don't like the samples, what do you
change? The training procedure? The architecture? If you have a setup you like
but slightly change the problem (eg generate reaction conditions with a solvent
mixture instead of one solvent), what parts of the previous setup do you expect
to transfer? Since the model architecture needs to change for the extra output,
how should that affect training/sampling?

These tricky questions are much simpler with modular algorithms: in each case a
particular module is implicated, and the desired outcome of the change to that
module should be reasonably clear.

## How is modularity in BO undersold?

This is the crux of the post: in my interactions with practitioners, very few
people seem to recognize and take advantage of BO's modularity, even when it is
the sensible thing to do. I attribute this to several causes:

1. **"Monolithic" algorithms**: many BO papers give a unified name to their
   model/acquisition function/optimizer setup. For example, the
   [ChemBO](http://proceedings.mlr.press/v108/korovina20a.html) paper uses a GP
   with a special optimal transport kernel, and an optimizer based on "walks"
   in synthesizable molecule space (they leave the acquisition function a bit
   variable). This gives the impression that these parts should be used as a
   _package_ rather than as independent modules.
2. **Biased experiments**: beyond simply giving their combination a name, many
   papers conduct an ablation study to show that their combination is _better_
   than other combinations. I think this is just a response to reviewer
   pressures to 1) claim a novel methodological contribution 2) show that the
   novel method is better than comparable non-novel methods. Inevitably I think
   all these comparisons are biased: the authors just run experiments until
   they find one where their method works better, or they impose a subtle
   constraint that handicaps other methods without reviewers
   noticing.[^handicap] However, practitioners might just take these results at
   face value.
3. **Emphasizing synergies**: a lot of BO papers describe computational
   synergies between their acquisition function and model, which also implies
   to practitioners that they should be used together.
4. **Lack of emphasis on modularity:** finally, aside from this blog post, I
   think there are very few written documents which explicitly describe this as
   a positive of BO. People just don't think about it as an advantage. Part of
   why I am writing this post is to change this impression.

[^handicap]: Examples of constraints authors might use to handicap other methods and bias the result towards showing that their method is better:
    
    - Authors might set an arbitrary cap on wallclock time, which seems fair,
      but actually they just spent time optimizing their method's code whereas
      other methods use unoptimized code and time out. The time cap is chosen
      so that other methods time out.
    - Authors might tune the hyperparameters of the baselines unfairly (eg "all
      baseline methods use a learning rate of 1e-3 for fairness", when that is
      actually a poor choice).
    - Initializing the optimization problem in a particular way (eg their
      acquisition function might be more exploitative, so they initialize with
      data close to the optimum, other methods explore around a lot while their
      method quickly exploits and finds the optimum).

Overall, this underselling seems _accidental_: it comes from a combination of
nobody explicitly advertising this and papers being slightly incentivized to
undersell modularity to emphasize the novelty of their methods.

## How to stop underselling modularity

First and foremost, I think BO researchers should explicitly mention modularity
as an advantage of BO when introducing it (eg in talks or in the introductions
of textbooks). Neither of the two most common "BO intro" references, [Shahriari
(2015)](https://ieeexplore.ieee.org/document/7352306/) and [Garnett's 2023
textbook](https://bayesoptbook.com/), discuss modularity as an advantage of
BO.[^whybo] The next researcher who writes a popular BO overview can (and
should) mention this!

[^whybo]: In fact, they don't really say much at all about why you would want to pick BO over other methods. They motivate BO independently using uncertainty / the black box nature of the functions.

Second, I think researchers should try to avoid writing "monolithic algorithm"
papers like XYZBO. If one does, please explicitly state something like
"although we choose this combo of model/acquisition function/optimizer, you
could really pick any subset of these that you want, they are conceptually
independent." This would avoid giving the impression that the algorithm is
explicitly _not_ modular. Similarly, if performing ablation studies on one
component (eg vary acquisition function with the same model), explicitly state
something like "note that the results might not transfer to all problem
settings", to avoid giving the impression that users should just stick with the
choice from the paper.

Lastly, it would be great if every paper had an appendix with an honest
description of why each component was chosen, what alternatives were
considered, and whether the authors guess practitioners should change them or
stick with the defaults. An explicit section about swapping out components of
the algorithm is a strong endorsement of modularity, and practical tips are
always appreciated by users (who never like "discovering the sharp edges" by
themselves). I don't think including this would ever hurt one's chances in peer
review. If authors are really worried, just add it after the paper is
accepted.[^peerreview]

[^peerreview]: I'll take the opportunity to criticize peer review a bit.
    
    1. Reviewers hardly read the appendix anyway.
    2. Bad reviewers basically stop caring after the paper is accepted.
    3. Don't feel bad about manipulating reviewers who are silly enough to view
       an honest user guide as a negative feature of a paper.

## Conclusion

Modularity is great, let's stop underselling this feature of BO!

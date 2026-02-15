---
title: "Why I don't care about toy benchmarks in BO"
date: 2026-02-08T22:00Z
tags:
    - machine learning
    - bayesian optimization
    - opinion
    - _recent-highlight
has_math: false
---

A lot of Bayesian optimization (BO) papers include experiments on "toy"
functions. Examples of such toy functions are Ackley, Rosenbrock, Hartmann, and
Branin. I basically ignore these experiments when I read papers and skip to the
next section. When I review papers (and therefore cannot simply skip sections),
I find my eyes glazing over and feel bored: I don't care about these functions,
don't care about the results, and don't really understand why the authors ran
this experiment.

For a while I assumed every BO researcher feels this way, but a bunch of recent
conversations have made it clear to me that many people do care. So, in this
post I explain why I don't care at all about benchmarks on toy functions (and
why you shouldn't either).

<!-- TEASER_END -->

## The main issue is transferability

Toy functions have known optima, and therefore running optimization on them is
a pointless task. In isolation, the knowledge of which algorithms perform best
on toy functions is a useless bit of trivia (since nobody is going to deploy
them in practice to optimize these specific functions). I don't think even the
most ardent supporter of toy benchmark functions would dispute this. Instead,
they claim that the value lies in some finding of the benchmark being
_transferable_ to settings we actually do care about (real world problems). I
think this is the core of the disagreement: I simply don't expect these results
to be transferable at all to real-world settings. That will be the crux of this
post.

Before getting to that, let's clear away two assumptions. The first is that I'm
basically _guessing_ that the point of toy benchmark experiments is to make
statements about real-world problems. Unfortunately, the scientific rigor of ML
is so poor that most papers don't even state why they do the experiments they
do or the scope of the results claimed, leaving it up to the reader's
imagination.[^empirical] If you imagine something different when you see these
experiments that's ok, but the position argued in this post might not make
sense. I am arguing against how _I_ believe _most people_ interpret these
experiments.

[^empirical]: I liked the paper [Position: Why We Must Rethink Empirical Research in Machine Learning](10.48550/arXiv.2405.02200) for its explanation of this (even though the paper was a bit too verbose). To paraphrase, other sciences usually have an explicit goal of what they are trying to measure, and try to establish "validity" of the metric they are using (ie "does it actually measure what we want to measure"). Not only does ML not really try to establish the validity of its metrics, it usually doesn't even specify what it is trying to measure.

The second is that there are many possible "real-world" experiments. When I use
this term in this post, I mean the set of applications where BO is most often
proposed as a desirable solution, which I think is:

- ML hyperparameter search
- Scientific discovery (small molecules, proteins, and materials being top
  spaces)
- Chemical reaction optimization (choosing temperature, concentration, solvent,
  etc)
- Engineering design (eg choosing which wing design to simulate)

Of course there are other problems, and sometimes real-world problems that
highly resemble toy benchmarks. I'm assuming in this post that this is highly
exceptional, and most real-world problems look very different than benchmarks.

## Too many things change to expect toy benchmark results to transfer

In short, the answer is that _too many things change_ for me to reasonably
expect trends observed in benchmark problems to also hold in real-world
problems. BO algorithms are _very_ sensitive to changes, eg changes in model
hyperparameters, acquisition functions, etc. In my experience playing around
with many algorithms in my PhD, changes in parameters can significantly change
both absolute performance, and performance relative to other algorithms.
Therefore, in the toy benchmark -> real-world function transfer, I simply see
too many things change to expect trends to hold. Let's go through some.

### Input space changes mean _you can't even run the same algorithm_

Almost all toy benchmarks are in d-dimensional Euclidean space, while most
real-world problems have at least some discrete element. Continuous to fully
(or partially) discrete is a massive change. First, it often requires a
different model to be used than the one chosen for benchmarking (eg a
stationary GP is not even well-defined on a space of graphs). Even if the same
model can be used, the acquisition function optimizer probably needs to change,
since pure gradient descent on the inputs is no longer possible.

A second (related) concern is that the _bounds_ of the input space can change.
Toy benchmarks usually assume a unit hypercube of some kind, whereas real-world
problems might be unbounded for have unknown bounds.

Overall, this puts two holes on any claims of transferability of conclusions.
First, if the algorithms studied _literally cannot be run on real-world
problems_, arguably the counterfactual of running the algorithms on real-world
problems _doesn't even exist_, so there is no "transfer" possible. If,
alternatively, you include changing core parts of the algorithm as part of the
process of "transfer", experience tells me that changing the model and
acquisition function optimization are some of the biggest possible changes in
the BO loop, ones that affect optimization performance in ways that are
difficult to predict, making conclusions less likely to transfer.

### Function being optimized

Benchmark functions are, usually, relatively smooth functions with no
pathological features that defy modelling assumptions: things like
discontinuities (or sharp jumps), varying smoothness, or different "regions"
with qualitatively different behaviour. Real-world functions can have all of
these. Therefore, even when using a "standard" model like a stationary GP, the
model is far more likely to be misspecified, and small differences in
misspecification could significantly change BO performance.

### Biased starting data causes modelling issues

BO benchmark problems are usually randomly initialized, while in real-world
problems one usually starts optimization from whatever previous data is
available. This data is usually quite biased: eg biased to one region of input
space, biased towards one mode, biased towards being close to optimal or far
from optimal (depending on the problem). Unfortunately, biased data causes
modelling issues.

The most common way to fit models in BO is by maximum likelihood (eg maximizing
marginal log likelihood to set GP hyperparameters), which balances model
"simplicity" with data fit. With biased data, this has two important effects:

1. It often selects for models which assume the "bias" in the biased data is
   present uniformly.
2. When parameters are underspecified, it picks the strongest and most
   simplifying assumption by default.

Here's a semi-real example in drug discovery, using an exact GP model (assuming
molecules are represented by vector features). In the "lead optimization" phase
of drug discovery, the starting data probably comes from the "hit ID" phase,
which are all structurally similar and all unusually active, derived from the
same initial "hit" molecule. First, the model is highly incentivized to learn a
mean near the starting data mean (assuming a constant mean function) and kernel
amplitude equal to starting dataset variance. While this set of parameters
explains the starting data well, it severely overestimates the activity of
molecules similar to the starting data, which are mostly not active at all.
Second, having never seen any 2 data points that are very far away from each
other, the model will not have good data to confidently set the GP lengthscale
parameter. Maximum likelihood highly incentives large lengthscale values (this
improves the "data fit" ter), and therefore the model will select the largest
plausible lengthscale compatible with the current data. Unfortunately, this
will probably mark structurally distinct molecules as more similar to training
molecules than is reasonable, causing the GP's predictive variance to be small.
Overall, the result is a model that confidently predicts almost all molecules
to be strong actives.

The best argument I've heard against this is that the initial random sampling
should be viewed as a core part of the BO procedure, not just a placeholder
initialization strategy. Perhaps there is some merit to this- random sampling
is a counter against dataset bias. But it is impractical for two reasons.
First, in situations where function evaluations are really expensive (eg lab
experiments with molecules), nobody wants to spend tons of money on random
initialization. Second, in more complex input spaces (eg molecules), it's not
even clear what an appropriate "random" distribution is. There is no analogue
to U(0, 1) or N(0, 1).

### Unrealistic state of knowledge

This applies if you take [my previous
advice](/blog/2026-01-25-model-centric-bo/) and aim to start BO with a model
that roughly captures your probabilistic belief about the function f at the
start of optimization, rather than just leave model selection as an internal
part of the BO algorithm. Toy benchmarks don't really simulate a realistic
"state of knowledge" that could be used to influence model fitting. On one
hand, BO researchers deliberately avoid biasing algorithm with knowledge about
the location or value of the optimum, even though this is actually known and
probably would help the algorithm perform better. On the other hand, the rough
level / kind of smoothness _is_ known and _is_ used implicitly when the BO
model creator selects a model class (eg Matern vs RBF kernel).

Real-world problems don't have this distinction of knowledge we "can" and
"cannot" use- we can (and should) use all knowledge. In fact, I bet it's
actually more common in practice to have an idea of the optimum's location and
value but _not_ the smoothness of the function- the opposite case to standard
BO practice.

Overall though, the bias against using knowledge about the problem probably
means that toy benchmark results are based on models which are overly "broad"
compared to real-world models, and I expect real-world problems to often use
"narrower" models.

## I don't believe in "performance floor"

Some people might accept that claims like "algorithm A outperforms algorithm B"
might not hold between toy benchmarks and real-world problems, but advocate for
a lesser version of the claim: "any algorithm that performs well on real-world
problems should _at least_ perform well on toy benchmarks". Therefore, one
could argue, toy benchmarks simply enforce a "floor" on performance, and not
clearing this floor means an algorithm is not worth considering for real-world
problems.

I don't believe this either, for largely the same reasons as above. Too many
things change, and it isn't too hard to imagine an algorithm that performs well
in practice but does not perform well on toy benchmarks.

For example, a BO algorithm which expects noisy, non-stationary data may use a
GP model with a smaller lengthscale. In relatively smooth BO benchmarks, this
would cause the algorithm to spend a lot of time doing local exploration,
rather than doing large leaps towards the optimum, and therefore it's
performance might be relatively poor. It would be erroneously to discard this
algorithm as "poor" though, it just makes a different set of assumptions that
are not valid in the circumstances of the benchmark.

Put another way, I think the same argument as above also applies in reverse:
there are too many changes _from_ real-world problems _to_ toy benchmarks to
expect performance results to transfer between these settings.

## No "insight" either

Aside from conclusions transferring from toy benchmarks to real-world
scenarios, another purported use of benchmark is to gain "insight" or
"understanding" of BO methods. Many toy benchmark problems are simple or have
one "difficult" component (eg 2 modes), and can be used to study how different
algorithms handle these scenarios. I agree that toy benchmarks have the
_potential_ to yield such insights, but as they are currently used they do not
yield any. This is because, in general, only the optimization _performance_ are
shown and studied, not the actual actions of the algorithms in input space.
This limits insights to things like "this change makes performance worse" or
"this change makes performance better". I think the arguments from the previous
sections apply here: there are just too many changes from toy problems to
real-world ones to expect such trends to hold. I bet some algorithm behaviours
_could_ hold up between problems and models (eg "algorithm A prioritizes
uncertain points over certain ones"), but since these aren't reported there is
nothing to comment on.

## Conclusions

In this post I've outlined how a lot of things change between toy benchmarks
and real-world problems, and argued that it is therefore unlikely for results
on toy benchmarks to be transferable to real-world problems. For the same
reason, I also disagree that toy benchmarks can be used as a "floor" or
"filter" for all worthy algorithms to pass through. I concede there might be
scope for toy benchmarks to yield insights into algorithms' behaviour, although
the prevailing practice of just showing the optimization performance (and not
the actual underlying behaviour) prevents us from realizing this benefit. To
me, this completely defeats the purpose of running the benchmarks in the first
place, and hence I do not care about toy benchmarks.

When I've expressed this view in the past, I've sometimes gotten the
incredulous question "what should we do instead, not run _any_ standardized
benchmark?" My answer is yes, I'd rather see no benchmark than a flawed one (or
at the very least, it could just be put into the appendix). I'm not sure why so
many people find this shocking. To finish, I'd like to seed the reader with the
suggestion to seriously consider just not running toy benchmarks at all. It's
hard to deviate from established practice, but when the practice is not useful
I think it's what we should do.


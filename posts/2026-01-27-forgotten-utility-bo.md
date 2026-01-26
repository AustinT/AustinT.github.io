---
title: "We have forgotten about utility functions in BO (whoops!)"
date: 2026-01-27T00:00Z
tags:
    - machine learning
    - bayesian optimization
    - opinion
    - _recent-highlight
has_math: true
---

Bayesian decision theory is one of the best justifications for BO- particularly
for myopic acquisition functions like expected improvement. However, these
acquisition functions are only "optimal" if one's utility function is $u(y) =
y$ (the identity function). Have BO researchers (and BO users) basically
_forgotten_ to swap this out for "real" utility functions in practice? In this
post I argue that we have basically overlooked this detail (to our own
detriment). It's not _too_ hard to fix, but unfortunately the $u(y) = y$
assumption is actually quite deeply embedded, and completely removing it will
make things more complicated. Ultimately, despite the difficulty, I think we
should do it anyway.

<!-- TEASER_END -->

## Primer: how the utility assumption ends up in expected improvement

I will use the _expected improvement_ (EI) acquisition function as a
placeholder for utility-based acquisition functions in general, and present a
quick derivation. A better and more thorough derivation can be found in §5.2 of "Bayesian
Optimization" by Garnett.[^bayesoptbook]

[^bayesoptbook]: Website here: <https://bayesoptbook.com/>.

**Problem setting.** We are maximizing a noiseless function $y = f(x)$. We have an evaluation history $\{{(x_1, y_1), \ldots, (x_n, y_n)\}}$. We can query 1 more x location: what should we do?

**Utility Functions** the answer depends on what we want. There is an element
of risk/reward trade-off (eg should we do a risky evaluation which might be
very large or a modest point which we are more confident about), and also some
ambiguity about how the previous solutions should affect our decisions. EI
starts by making an innocent assumption: we only care about the _single best
point_ we evaluate. This means there is an incumbent best point

$$y^* = \max_{i\leq1\leq n} y_i$$

and, if our final evaluation returns $y_{n+1} < y^\*$
then that's ok, we will just go with $y^*$. Otherwise we will go with $y_{n+1}$.
We can only _gain_ from the final evaluation, not lose anything.

**Bayesian decision theory.** Next, Bayesian decision theory says that we
should make this decision by maximizing _expected utility_, which maps each
outcome through a utility function $u$ that says how "good" the outcome is.
Assuming $u(y_1, \ldots, y_n, y_{n+1})=\max_i y_i$ and doing the math, you get
an expected utility

$$ E_{y_{n+1}} \left[ \max\left(0, y_{n+1}-y^* \right)\right]$$

which is the expected amount of improvement (hence the name expected improvement).

**Summary.** The utility function appears when Bayesian decision theory is
invoked, and the utility of a _set_ of solutions is just the maximum value in
the set.

## What's wrong with this utility function?

Bayesian decision theory states that preferences over uncertain outcomes can be
cast as maximizing expected utility of _some_ utility function: ie for any
given set of preferences there must exist a utility function. It _does not_ say
that if you pick a utility function and maximize expected utility you will be
acting according to your preferences. Therefore, the utility function
fundamentally must be an _input_ to the problem, not something that can be arbitrarily set.

Digging into the assumptions behind expected utility a bit
further,[^expectedutilitypost] the utility function's values basically play 2
roles:

[^expectedutilitypost]: See [this post](/blog/2025-11-02-expected-utility/) for more details on these assuptions.

1. It _orders_ the outcomes (saying which outcomes are better and worse, and
   which are equivalent).
2. It defines the user's _risk reward_ over outcomes. Assuming $u(A) < u(B) <
   u(C)$ it assumes the user would be equally ok with receiving B with 100%
   chance or taking the gamble "A with probability p, otherwise C" where $p =
   \left(u(C) - u(B)\right) / \left(u(C) - u(A) \right)$.

$u(y) = y$ obviously correctly orders outcomes in the case of maximization
(where higher is always better), but who knows what the user's risk-reward
trade-off actually is? The bet with probability p is a highly specific
assumption that seems highly unlikely to hold for users in general. To make it
a bit more concrete, let's assume $y^* = 1$ (ie best score found so far is 1).
If presented with the options:

1. 1.5 (100% probability)
2. 0.5 (50% probability), 2.1 (50% probability)
3. 0.9 (90% probability), 7 (10% probability)

Expected improvement under the standard utility function would choose option 3
because it has the highest expected improvement, even though it is the riskiest
option.[^EIvalues] To give a stylized real-world example of where this is might
be unreasonable: in drug discovery there are often competitor drugs, and one's
drug needs to be _better_ in order to get approved. If the competitor drug has
a potency of 1, then _matching_ them doesn't succeed: you need to be better. I
bet many decision makers would prefer option 1 in this case: it gets you "over
the line" with certainty. Their utility function would probably be flat before
$y=1$, then increase.

[^EIvalues]: EI values are 1: 0.5 2: 0.55 3: 0.6.

## How did this utility function come to be used everywhere?

I'm not sure- and don't really have time to go to the literature to find out.
My guess is just a by-product of how papers are written. Academic papers aren't
really "users" of the algorithms so they don't have strong preferences that
would form the basis for a utility function. At the same time they need to make
_some_ choice to run experiments, and a choice like $u(y) = y$ seems more
"neutral" than something like $u(y) = \min\left(y, 3\sqrt{y} -1\right)$, plus
it allows EI to be computed analytically, so authors just go with it. Authors
of other papers then reimplement the method and use the implementation in the
original paper with $u(y)=y$. Over time, the original utility function gets
forgotten and users concentrate on the case that is actually implemented and
studied.

My overall point is that using $u(y)=y$ was probably _not_ a deliberate choice
or statement about how BO methods should be used in general, it was just a
simple design choice that stuck around.

## Warped GPs are not the answer

A plausible-sounding workaround is the following: instead of creating a
surrogate model of the unknown function f(x), create a surrogate model of
$g(x)=u(f(x))$ and run BO with this. After all, $g(x)$ is effectively just
another black-box function. This model, commonly called a _warped
GP_[^snelson2003], might seem to be the ideal solution: it uses the utility
function without needing to adjust the underlying BO algorithm. Problem solved?

[^snelson2003]: Original paper: [Warped Gaussian Processes, NeurIPS 2003](https://proceedings.neurips.cc/paper/2003/hash/6b5754d737784b51ec5075c0dc437bf0-Abstract.html).

Unfortunately I think not. The main issue I foresee is that real-world utility
functions u might violate a lot of assumptions commonly made about surrogate
models: for example, differentiability, continuity, or stationarity. For
example, consider the drug discovery example I gave earlier about finding
molecules that bind better than a competitor's molecule. A lot of molecules
with binding ≤ 1 will have a utility score of exactly 0, with a sudden jump in
g once binding exceeds 1. This is probably hard to fit a model to: it turns
what might be a smooth relationship between structure and binding into a
discrete jump, and probably masks the learning signal because a lot of
improvements in binding (eg 0.7 -> 0.8 -> 0.9) will just look like a constant
zero. It's also probably harder to fit a good noise model in utility space. An
actual binding measurement probably has (somewhat) Gaussian noise of a similar
magnitude for most binding strengths. However, mapped through a utility
function to give noise on g, the noise would be highly non-Gaussian and
therefore harder to model.

A secondary issue is that such a model goes against the decision-theoretic
roots of BO, which fundamentally posits that outcomes and preferences are
conceptually separate. I think this separation is one of BO's biggest
strengths, especially when compared to other methods (like generative models)
which mix preferences and beliefs together in a confusing way (and are thus a
bit harder to tune and use).

Of course we can abandon principled appeals to theory, it's not _impossible_ to
overcome these modelling difficulties. In this sense warped GPs _could_ work.
The main point I want to convey is that they are a difficult choice that comes
with a lot of "hidden" drawbacks, and therefore we (the BO community) shouldn't
just accept them as the sole solution and move on.

## Properly supporting more general utility functions might be hard

If we stick to the principles of Bayesian decision theory, the "right" way to
handle utility functions is as an _input_ to the BO loop. A surrogate model is
constructed, and the acquisition function should be computed on the _utilities_
of the output, not the raw outputs themselves. Unfortunately this introduces a
lot of potential difficulties.

To start, what restrictions should exist on u, if any? If u is itself a black
box function then something like numerical integration would be necessary to
evaluate the acquisition function at any point. That adds a lot of computation
cost, and that's just for a _pointwise_ estimation, not even the _gradient_
$\nabla_x \alpha(x)$.

I think we can't totally dismiss this worst-case scenario, but intuitively it
feels like most users should be happy with _analytic_ utility functions,
possibly even ones which are continuous, and maybe even differentiable (almost
everywhere). This includes functions like:

- $u(y) = y$
- $u(y) = \sqrt{y}$
- $u(y) = \min\left(y, 3\sqrt{y}-1\right)$

This feels like a pretty broad class of functions for users to express their
preferences with, and one which is more amenable to BO. Acquisition values may
still need to be computed with numerical integration, but I bet this could be
partially cached or done analytically (at least with Gaussian posteriors). You
should even be able to compute acquisition function gradients using the
analytic derivative of u.

However, even in this more optimistic case BO software would look a lot more
complicated: essentially every acquisition function would have custom
computational requirements which need to be specified by the user (because
having BO researchers provide out of the box utility functions sort of defeats
the point of the user providing this as an input).

## Summary: this is tough but worth it

Given how hard it would be to retrofit user-provided utility functions onto BO, should we (the BO research community) just not do it? While the lazy option is certainly tempting, I think at least _some_ people in the BO community should work on this. Here is what I think pursuing this could lead to:

- A way for the user to input their risk/reward preferences, giving them more
  direct control over the explore/exploit behaviours of BO algorithms
  (something which many users would like).
- A more principled starting point for cost-aware BO, which usually needs to
  assume a value-cost trade off.
- Automatically the cases of maximization, minimization, and targeting a
  specific value get handled in a unified way (via the utility function). No
  more confusing the EI equations for maximization vs minimization!
- A utility-based framework naturally generalizes to multi-objective
  optimization (the utility function is basically a kind of scalarization).

Overall I think there is potentially for at least one good JMLR-style paper
here, or a NeurIPS/ICML/ICLR paper introducing a software library supporting
arbitrary utility functions for BO. Plus, there are some acquisition functions
without a clear grounding in Bayesian decision theory (eg UCB), and some
theoretical work putting utility functions in would be welcome.[^ucb] If any of
this sounds interesting, feel free to get in touch with me.

[^ucb]: Eg for UCB I imagine the equivalent notion would be an upper bound on the _utility_ (rather than an upper bound on the function), but I'm not sure if all the desirable properties of UCB would transfer to this case.

**Final thought**: remember, in Bayesian ML we do things not because they are
easy, but because they are _right_.


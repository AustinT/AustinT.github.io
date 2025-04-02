---
title: "Why your active learning algorithm may not do better than random"
date: 2025-04-02
tags:
    - machine learning
    - speculation
has_math: false
---

I am a big fan of active learning, but I am also acutely aware of its potential
failure modes. A common failure mode is _random-like_ performance: achieving no
better "success"[^success] in picking points than a _random_ policy. Indeed, it
is possible to experience this when the implementation is flawed.[^wrong]
However, in some problems it _may not be possible_ to beat random-like
performance. In this post I try to explain why.

<!-- TEASER_END -->

<div class="alert alert-info">
This is a "quickpost": a post which I have tried to write quickly, without very much editing/polishing.
For more details on quickposts, see
<a href="/blog/2025-02-11-lowering-quality/">this blog post</a>.
</div>

[^success]: This could be model accuracy, regret of the points chosen, or something else.

[^wrong]: E.g., a bug in the code, or poorly tuned parameters.

## Why would you expect active learning to be BETTER than random?

The general premise of active learning is that you can use a model to select
the most "informative" data points to label. For this strategy to be better
than random, you would need:

- High _variation_ in the "informativeness" of potential data points (if all
  points are equally informative then no policy will be better than random).
- A model which can judge "informativeness" (e.g. by having well-calibrated
  uncertainty).
- Agreement between "informativeness" and "performance".[^agreement]

These tend to all be true in the "toy" problems studied in active learning
papers, but may be _completely false_ in practice.

- Data pools may be very homogeneous and full of similar points.
- Neural networks are often overconfident in their own predictions.
- There are many different notions of "information" and many different metrics,
  and they can't all match each other...

[^agreement]: For example, in an active learning classification task, if "informativeness" is a model's predicted uncertainty, and "performance" is the classification accuracy of the model trained on all data so far, it is possible that the most "informative" examples to label are outliers, and labelling them does not meaningfully increase the performance on the test set.

## Practical example: molecule design

I focused on molecule design in my PhD and saw many papers use active learning
to select promising molecules, but achieve poor performance. This is probably
because:

- The space of all small molecules is ENORMOUS (maybe `1e60`). For any
  realistic training set, there is always an infinite supply of molecules
  dissimilar to _every_ molecule in the training set, and are therefore highly
  informative.
- Getting uncertainty estimates is hard, and many papers use questionable
  techniques like "approximate Bayesian neural networks with variational
  inference", which may not work well.
- Often what people want from active learning is "find the best molecules" or
  "train a very accurate model over a narrow region of chemical space", but the
  model just picks "outlier" points from the vastness of molecule space.

## Will active learning be better than random on *my* problem?

Obviously I can't say without knowing what your problem is. My general checklist would be:

1. **What is the space of points you are choosing from?** The smaller the set,
   the stronger a random policy will be in general. Large sets with many
   similar data points and a small number of "outlier" points will make a
   random policy perform worse, but _only_ if the optimal policy is to _pick_
   the outlier points. If the outlier points are, not helpful then they might
   just "distract" an active learning algorithm.
2. **What model will be used to make decisions?** Active learning is very
   sensitive to the model. If your model generally _underfits_ the data (eg a
   Bayesian model with a strong prior), then most data points will probably be
   similarly "informative". If your model _overfits_ the data, then it might
   not provide reliable uncertainty estimates. If your model is some kind of
   "local" model (eg a kernel method or k-nearest neighbors) then the model
   will be prone to picking "distant" data points (and may possibly fall into
   the trap of querying an endless supply of "distant" data points). My overall
   recommendation is to have a model with a fairly _good_ fit, erring on the
   side of underfitting if possible.
3. **What is your objective?** The objectives "improve model accuracy" and
   "optimize a black-box function" are well-studied. Other objectives are much
   less well-studied. If the goal is "improve model accuracy", ensure that the
   pool set is not *too* different from the test set.

Remember that these are just my guesses; your mileage may vary.

## Conclusions

Although there are many cases when active learning might not be better than
random, I am still enthusiastic about it because I think many problems _are_
amenable to active learning, or _can be modified_ to be more amenable.
Nonetheless, I hope this post explains why not all active learning projects
might be successful.

<div class="alert alert-success">

This post was checked for LLM alpha (see <a
href="/blog/2025-02-24-llm-alpha/">this blog post</a> for details). I asked
Claude Sonnet 3.7 about why active learning may be no better than random
and it only said:

<ul>
<li>In the very early stages with extremely few labeled examples, random sampling might occasionally outperform active learning</li>
Active learning can sometimes focus too narrowly on certain patterns and miss important outliers</li>
<li>The effectiveness depends on the quality of the informativeness measure used (uncertainty sampling, query-by-committee, expected model change, etc.)</li>
<li>Performance advantage varies by dataset complexity and model type</li>
</ul>

</div>

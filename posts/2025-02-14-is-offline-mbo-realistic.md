---
title: "Is offline model-based optimization a realistic problem? (I'm not convinced)"
date: 2025-02-14
tags:
    - machine learning
    - speculation
has_math: false
---

<div class="alert alert-info">
This is a "quickpost": a post which I have tried to write quickly, without very much editing/polishing.
For more details on quickposts, see
<a href="/blog/2025-02-11-lowering-quality/">this blog post</a>.
</div>

Offline model-based optimization (OMBO in this post) is essentially 1-shot
optimization using a fixed dataset. You see data, do whatever you want, then
propose a batch of query points, which are then evaluated. Hopefully, one (or
most) of the query points are optimal (or near optimal). End of task.

<!-- TEASER_END -->

I see lots of machine learning papers about OMBO at top conferences.
Unfortunately, I'm not convinced that OMBO actually is a real problem. This
post is my attempt to explain why.

## Main reason: do you ever have "one attempt"?

When papers do motivate OMBO, the motivation is usually something like "many
domains have expensive or dangerous experiments and can't be trained online
reasonably, meaning that no feedback is given during optimization". Put another
way: the algorithm has only _one attempt_ to propose solutions. Unfortunately,
none of the common example domains given in papers actually seem to have this
restriction:

- **Chemistry/drug design/protein design**: yes, experiments are expensive
  here. That being said, drugs are _never_ designed in one shot. Projects
  include many iterations, even though the number of compounds tested is small
  by ML standards (hundreds to thousands, but never millions or billions).
- **Materials**: same as chemistry: expensive experiments, multiple design
  iterations.
- **Robotics**: yes, practical safety considerations mean you will probably
  never do real-world RL from scratch, and will try to learn a policy using
  offline data. But this policy probably _will not_ be learned purely offline
  (at the very least, people would test it online).

Assuming OMBO researchers agree with this, the best argument I can think of for
studying offline optimization is something like:

> Yes, real world problems are not exactly "offline", but an optimization task
> with lots of offline data and only ~10 batches for evaluation is much closer
> to the offline than to the online + on-policy setting often studied in RL
> (with millions of online optimization steps). We would also like to see
> progress in each batch. By studying the one-batch setting, we can develop
> policies which can then be applied repeatedly ~10 times in real world
> problems.

However, this argument has an important flaw: **optimal N-step policies are
usually very different than optimal 1-step policies applied N times**! This has
been worked out repeatedly in Bayesian optimization, bandits, RL, and probably
lots of other subfields which I am not aware of (more in
footnote[^myopicintuition]). Therefore, studying offline optimization is
_probably not_ a good way to build up to online optimization.

[^myopicintuition]: If you have not come across this conclusion seems odd to you, consider why an optimal 2-step optimization policy might differ from the optimal 1-step policy applied twice. A 2 step policy could, in the first step, explore widely to find potential new optima, then in the second step choose a less diverse query set around a narrow set of optima. However, this initial "exploration" step is likely not an optimal 1-step policy, and so the optimal 1-step policy applied twice will probably look like exploitation (twice). Note that these behaviors can vary hugely in different problem settings.

Another possible argument for offline optimization is:

> Batch optimization algorithms usually attempt to approximate an optimal
> N-step policy *without* observing rewards for intermediate actions. This
> becomes harder and harder as the batch size grows. Therefore, for a
> sufficiently large batch size, online optimization is effectively the same as
> offline optimization.

I am also not convinced by this argument for two main reasons:

1. Nobody is forcing you to approximate N-step policies when choosing a batch.
   If anything, heuristics often seem to work well in practice.
2. In problems whose search space is much larger than the batch size (eg
   molecules), the "explore then exploit" strategy described in the previous
   footnote[^myopicintuition] is still possible, because one can explore almost
   infinitely.

So, after really trying to "steelman" the applicability of offline
optimization, I can't find a good argument for it.

## Secondary reason: why "model-based"?

This is much less substantial than the previous reason, but it seems like a lot
of this literature assumes that the only plausible way to solve OMBO problems
is to train a surrogate model on existing data, then optimize with respect to
that surrogate model (using regularization of some kind to avoid crazy
solutions and surrogate model "hallucinations"). Hence, "model-based" goes into
the problem name. Of course, this is not true: one could also use model-free
methods like genetic algorithms (essentially proposing small variants of the
best points in the dataset). Yet, most papers don't really consider such
methods?

This could be resolved by papers simply calling it "offline optimization"
instead of OMBO.

## Final aside: design bench

This is a bit separate from my skepticism of the OMBO problem setting, but it
seems to me that most papers in this field use just a single benchmark with ~8
tasks: [Design Bench by Trabucco et
al.](https://proceedings.mlr.press/v162/trabucco22a.html) This does not seem
like a healthy focus for a subfield that has gotten as big as OMBO, especially
when all of the problems in the benchmark seem a bit contrived. If people in
this field are serious about making progress (and I'm wrong about the overall
setup being unrealistic), I think it's time for somebody to make an improved
benchmark.

## Conclusion

In this post, I basically said:

- OMBO assumes just one shot for optimization, which is *not* a common setup in
  chemistry/materials/robotics (at least not to my knowledge).
- OMBO is poorly named because model-free approaches are also valid.
- OMBO could benefit from more benchmarks.

I plan to post this to Twitter/Bluesky. If you disagree with anything in this
post, please do comment! I would love to learn why I am wrong about this.

---

## Addendum: responses to my Twitter post

The best counter-arguments I heard after sharing this post were:

- It could be useful for people who want to try ML out a little bit without
  committing to multiple rounds of optimization.
- It could be useful for the last round of optimization.

I don't disagree with either of these reasons, but they seem sufficiently niche
that I would not want an entire subfield to be based around them...


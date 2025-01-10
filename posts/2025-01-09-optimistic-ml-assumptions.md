---
title: "What ML researchers and users get wrong: optimistic assumptions"
date: 2025-01-09
tags:
    - speculation
has_math: false
---

ML is often done poorly, both by "ML experts" (by which I mean people who
understand the algorithms but not the data) and "ML users" (by which I mean
people who understand their data, but not the algorithms). I think the cause is
often over-optimism, although about different things:

<!-- TEASER_END -->

- When designing algorithms, *ML experts make optimistic assumptions about the
  data* (eg it is IID, lies on a low-dimensional manifold, has sub-Gaussian
  noise)
- When selecting algorithms for their data, *ML users make optimistic
  assumptions about behavior of the algorithms* (eg it is robust to outliers,
  will discover hidden "truths" in data, will always be better than predicting
  the mean)

In reality, these assumptions are usually unwarranted. It is helpful to keep in
mind:

- *ML experts*: there is a whole universe of crazy data out there. Some data is
  so noisy that it's basically just noise. Some data is aggregated from 100
  heterogeneous sources. Data will have random labelling artifacts (eg, some
  survey respondents will pick A for every answer just to complete the survey
  quickly). Every time you add an assumption to your analysis, you reduce the
  class of problems your method can be applied to. If you don't document these
  assumptions clearly, people *will* misuse your algorithms.
- *ML users*: AI is not magic and is often more brittle than you think.
  Algorithms can "overfit" to your data. LLMs make things up. Test set loss
  only estimates generalization if drawn from the same distribution you will
  see at deployment (among other conditions). I like [this
  image](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_001.png)
  from `scikit-learn` which shows how common clustering algorithms can give
  weird results, even on simple toy datasets.

---
title: "Generic recommendations for cheminformatics models."
date: 2025-04-01
tags:
    - machine learning
    - chemistry
    - speculation
has_math: false
---

I was recently asked via email for my thoughts on which models to use _in
general_ for molecular property prediction. I'm sharing my responses publicly
in case they are useful.

<!-- TEASER_END -->

---

**Q1**: what kinds of models have you used for cheminformatics problems?

**A1**: I have used a lot of GP models, but also graph neural networks, random
forest, and sometimes support vector machines. I would use Botorch / Gauche for
GPs, scikit learn for random forest, and Pytorch + deepchem for graph neural
networks. Kernels: often standard kernels like RBF or Matern, but sometimes
discrete ones like the Tanimoto kernel. Note however that I don't have a _ton_
of experience with real-world datasets since my PhD work was in ML methods and
used clean, toy(ish) dataset.

**Q2**: how do you do feature selection before GP regression?

**A2**: I think feature selection should be done together with model fitting. A
semi-automated method for this is to use automatic relevance determination
(ARD): essentially choosing a separate lengthscale for each input feature
dimension. Large lengthscale values essentially cause a feature to be ignored.
Beyond that I think model selection is highly problem-dependent.

**Q3**: would you recommend BNNs (Bayesian neural networks) for larger datasets?

**A3**: In principle yes, I would recommend BNNs for larger datasets, although
"truly Bayesian" neural networks are very computationally expensive, and people
generally use approximations. Not all approximations are equal. I would use
"deep ensembles" as a simple default. This is just a fancy name for "train N
neural networks with separate initializations and use their distributions of
predictions as samples from p(y|x)"

**Q4**: What are recommended methods for doing multi-target GP regression?

**A4**: I have not worked with multi-target GPs myself but am interested in
looking more into this. I think separate GP models are one sensible approach.
Another sensible approach is the "coregionalization" kernel where you jointly
model all targets using the kernel k(x1, target1, x2, target2) = k_x(x1, x2)  *
k_t(target1, target2). k_x can be a typical molecule kernel, k_t is some kind
of "target similarity" (which would depend on your target so I don't have a
good recommendation for this). k_t=0 means the targets are unrelated, and if
k_t(target1, target2) = 0 whenever target1 ≠ target2 this is mathematically
equivalent to an independent GP model for each target. This is a good starting
point but I can't promise how well it will work.


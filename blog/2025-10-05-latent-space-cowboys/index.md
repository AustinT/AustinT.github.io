---
title: "Latent Space COWBOYS: a VAE-BO method I can actually buy into!"
date: 2025-10-05
tags:
    - bayesian optimization
    - machine learning
    - opinion
    - research papers
has_math: true
---

I am generally pessimistic about BO (Bayesian optimization) methods which use
VAE embeddings as part of the model. Mostly this is because distance in a VAE's
latent space has no reason to correlate with distances in property space
(unless trained for it), and because training with labels is basically deep
kernel learning which usually overfits[^1]. However, I recently came across the
paper "_Return of the Latent Space COWBOYS: Re-thinking the use of VAEs for
Bayesian Optimisation of Structured Spaces_"[^2] and quite liked the idea,
ending my long-standing streak of disliking every VAE-BO paper I read.

<!-- TEASER_END -->

[^1]: See _The promises and pitfalls of deep kernel learning_ (<https://proceedings.mlr.press/v161/ober21a.html>)

[^2]: ICML 2025. See <https://arxiv.org/abs/2507.03910>

The key idea is basically to use the VAE as a tool for _acquisition function
optimization only_: actual BO modelling is handled by an external model. This
allows (some) continuous optimization methods to be used _without_ requiring
that the VAE's latent space is a key feature of the model. They use the VAE +
GP combo essentially as a _likelihood_ function on the latent variable $z$[^3],
and apply MCMC methods normally meant for posterior inference in Bayesian
models.

[^3]: Details in §5.1 of the paper

Overall the idea is sound and I appreciated the experiments. That being said, I
would have liked it if Tanimoto GP + Graph GA optimizer was included as a
baseline to compare latent space vs non-latent space methods, but that doesn't
fundamentally change my evaluation of the paper.


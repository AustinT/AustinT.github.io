---
title: "Taking the V out of VAEs: long live KL-regularized autoencoders!"
date: 2025-04-24
tags:
    - machine learning
has_math: false
---

I recently read [this post about generative modelling in latent
space](https://sander.ai/2025/04/15/latents.html#) by Sander Dieleman and
agreed strongly with the following quote (copied verbatim except for typo
correction):

<!-- TEASER_END -->

> KL regularisation, on the other hand, is a core part of the traditional VAE
> setup: it is one of the two terms constituting the evidence lower bound
> (ELBO), which bounds the likelihood from below and enables VAE training to
> tractably (but indirectly) maximise the likelihood of the data. It encourages
> the latents to follow the imposed prior distribution (usually Gaussian).
> Crucially however, the ELBO is only truly a lower bound on the likelihood if
> there is no scaling hyperparameter in front of this term. Yet almost
> invariably, the KL term used to regularise continuous latent spaces is scaled
> down significantly (usually by several orders of magnitude), all but severing
> the connection with the variational inference context in which it originally
> arose.
>
> The reason is simple: an unscaled KL term has too strong an effect, imposing
> a stringent limit on latent capacity and thus severely degrading
> reconstruction quality. The pragmatic response to that is naturally to scale
> down its relative contribution to the training loss. (Aside: in settings
> where one cares less about reconstruction quality, and more about semantic
> interpretability and disentanglement of the learnt
> representation, increasing the scale of the KL term can also be fruitful, as
> in beta-VAE.)
> 
> We are veering firmly into opinion territory here, but I feel there is
> currently quite a bit of magical thinking around the effect of the KL term.
> It is often suggested that this term encourages the latents to follow a
> Gaussian distribution, but with the scale factors that are typically used,
> this effect is way too weak to be meaningful. Even for “proper” VAEs, the
> aggregate posterior is rarely actually Gaussian.
> 
> All of this renders the “V” in “VAE” basically meaningless, in my opinion –
> its relevance is largely historical. We may as well drop it and talk about
> KL-regularised autoencoders instead, which more accurately reflects modern
> practice. The most important effect of the KL term in this setting is to
> suppress outliers and constrain the scale of the latents to some extent. In
> other words: while the KL term is often presented as constraining capacity,
> the way it is used in practice mainly constrains the shape of the
> latents (but even that effect is relatively modest).

KL-regularized autoencoders are just one part of a whole family of regularized
autoencoders, some with a probabilistic interpretation (eg Wasserstein
autoencoders), others less so.

I will try to use the term "X-regularized autoencoder" myself in the future.


---
layout: default
title: Retrospective thoughts on my papers
---

# Retrospective thoughts of my papers

On this page I try to give an honest evaluation of the academic papers I have co-authored.
I am making this page because:

1. It might be hard to tell at a glance whether something in an academic paper will work in real life.
2. Because updating scientific papers is relatively uncommon, there isn't really a proper place for an author to state how their work looks in hindsight.

Note that this page does not serve as a comprehensive and up-to-date list of my publications
(see Google Scholar for that).
If you would like me to write about a specific article that is missing or would like an update
on an existing article, please send me an email and I will write an update.

Papers are listed in reverse chronological order.

## Retro-fallback: retrosynthetic planning in an uncertain world

- **Authoritative link:** <https://arxiv.org/abs/2310.09270>
- **Summary:** an algorithm to suggest synthesis routes for molecules using reaction uncertainty.
- **My contribution:** co-lead of the project and primary developer of the algorithm. Details in the paper's author contribution section.
- **Thoughts (as of 2023-11-24):**
  This is ongoing work so I cannot really offer a "retrospective",
  but barring significant advancements in single-step reaction prediction I think retro-fallback could
  be really useful in practice!

## Nonequilibrium sensing of volatile compounds using active and passive analyte delivery

- **Authoritative link:** <https://www.pnas.org/doi/abs/10.1073/pnas.2303928120>
- **Summary:** a sensor to analyze mixtures of volatile organic compounds using time-dependent diffusion and absorption into a photonic crystal.
- **My contribution:** I worked on this project during an internship from 2016-2017 (long before it was published). I did some analysis and designed some early machine learning algorithms to analyze the data (mostly SVMs).
- **Thoughts (as of 2023-11-24):**
  I think this was a cool project and that the underlying sensing technology could one day be deployed.
  However, the project evolved and changed a lot between the time I did my internship and the time it was published
  so I don't think I am in a good position to comment on the work as a whole.

## Tanimoto Random Features for Scalable Molecular Machine Learning

- **Authoritative link:** <https://arxiv.org/abs/2306.14809>
- **Summary:** scalable approximation for Tanimoto kernel (useful for GPs on molecules)
- **My contribution:** initiated project, co-developed minmax random features, did writing + experiments.
- **Thoughts (as of 2023-11-24):**
  This paper does what it says it does: provides an approximation to this kernel.
  I am happy that this paper made modest claims and demonstrated them,
  in contrast to many papers which support bold claims with shaky experiments.

## Retrosynthetic Planning with Dual Value Networks

- **Authoritative link:** unsure which link is authoritative, but here is the arXiv link: <https://arxiv.org/abs/2301.13755>
- **Summary:** apply reinforcement learning for retrosynthesis
- **My contribution:** not much: I had some early conversations with the main authors and contributed a bit of code.
- **Thoughts (as of 2023-11-24):**
  Let me preface by saying these are _my_ thoughts and do not represent the thoughts of the other co-authors.
  
  This algorithm does what it claims to do (produce possible synthesis routes),
  but I wouldn't actually deploy it in practice.
  Since single-step reaction models are imperfect I think this technique (and other similar techniques)
  will just learn to exploit the model.
  My vision for retrosynthesis is to accept the presence of imperfect models and try to model
  their imperfections (e.g. my "retro-fallback" paper).

  Also, as far as I can tell there is no publicly available code for this paper, which I think is shameful...

## GAUCHE: A library for Gaussian processes in chemistry

- **Authoritative link:** unclear, but here is the arXiv link: <https://arxiv.org/abs/2212.04450>
- **Summary:** paper accompanying software library for GPs on molecules
- **My contribution:** I contributed an implementation of the Tanimoto kernel.
- **Thoughts (as of 2023-11-24):**
  I have not really used this library (I mostly just use my own GP code).
  Last time I tried to install the library the recommended environment
  had conflicting dependencies that could not be resolved.
  I hope this is fixed...

## Meta-learning adaptive deep kernel gaussian processes for molecular property prediction

- **Authoritative link:** <https://arxiv.org/abs/2205.02708>
- **Summary:** meta-learning algorithm using GPs. It is general but we had the application of molecules in mind.
- **My contribution:** I had the idea and wrote a prototype algorithm, but Wenlin did the rest of the work.
- **Thoughts (as of 2023-11-24):**
  I think this is a solid algorithm which could be used for real-life problems,
  _if_ there is a relevant meta-dataset.
  I would be hesitant to just take our pre-trained model and apply it on a random new problem.

## DOCKSTRING: easy molecular docking yields better benchmarks for ligand design

- **Authoritative link:** <https://pubs.acs.org/doi/full/10.1021/acs.jcim.1c01334>
- **Summary:** benchmark to measure performance of machine learning algorithms for small molecules
- **My contribution:** I implemented most of the algorithms whose scores on the benchmark we reported.
- **Thoughts (as of 2023-11-24):**
  Although docking scores are not a great proxy for real assay data,
  I think this benchmark is a huge improvement over many common benchmarks
  and is currently underused by the community!

## Sample-efficient optimization in the latent space of deep generative models via weighted retraining

- **Authoritative link:** <https://arxiv.org/abs/2006.09191>
- **Summary:** ML algorithm to optimize structured inputs, e.g. molecules.
- **My contribution:** I conceived the project and performed the experiments / did writing jointly with Erik.
- **Thoughts (as of 2023-11-24):**
  This is the first paper that was really "mine".
  While there is nothing explicitly wrong in the paper,
  in hindsight the approach and methodology is more naive and less original than I previously thought.
  The algorithm proposed in the paper has two parts.
  - _The "weighted retraining"_: I think this is sensible and would expect it to work well on other problems.
    However, I do think it is basically an instance of an ["Estimation of distribution algorithm"](https://en.wikipedia.org/wiki/Estimation_of_distribution_algorithm)
    and am unsure whether it would work really better in practice than other EDAs.
  - _The "latent space optimization" (LSO)_: I tried to extend the LSO to other problems for ~1 year
    but had poor results. I think the fundamental difficulty is that it is at least as hard
    to create an informative probabilistic model in a continuous latent space
    as it is in a discrete space like molecules.
    In fact, it might even be harder: e.g. it is probably easier to specify a prior for smoothness with respect to molecular structure directly in molecule space than in some abstract latent space.
    I think the reason this method got strong results in our paper is because the objective we optimized,
    logP, is essentially just a proxy for molecular size and is easy to optimize by finding large out-of-distribution molecules.

    Overall I would _not_ recommend using LSO:
    instead I would create a model directly in whatever discrete input space is being used
    (e.g. a GP with the Tanimoto kernel for molecules) and optimize acquisition functions using genetic algorithms.
    I know there has been subsequent work on LSO which is more positive, but I think these works just
    lack strong BO baselines which don't use a latent space.

## Petroleomic analysis of the treatment of naphthenic organics in oil sands process-affected water with buoyant photocatalysts

This is the first paper which I contributed towards.

- **Authoritative link:** <https://www.sciencedirect.com/science/article/pii/S0043135418303737>
- **Summary:** uses floating nanoparticles to treat contaminated water.
- **My contribution:** I did some experiments for this paper during an internship in 2016.
- **Thoughts (as of 2023-11-24):** I did not participate in the writing so I don't have any strong opinions on the paper's claims and text. I did personally see the nanoparticles working though!

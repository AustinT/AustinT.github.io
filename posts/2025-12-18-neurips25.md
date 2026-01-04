---
title: "Review of NeurIPS 2025"
date: 2025-12-18
tags:
    - machine learning
    - _recent-highlight
has_math: false
---

I added the NeurIPS _workshops_ this year (not the main conference).[^1] Here
are my takeaways. I'll follow up with predictions for 2026 in a later post.

<!-- TEASER_END -->

(**NOTE**: I mostly attended bio/drug discovery/science workshops, so compared
to [last year](/blog/2025-01-01-neurips24-and-trends25/) my takeaways are much
more focused)

- Nothing really surprised me this year. Perhaps this is because I focused on
  things related to drug discovery, and by virtue of being with Valence I've
  kept up with this subfield pretty well throughout the year.
- Overall breakdown of papers seemed to be ~50% LLM stuff, ~30% diffusion
  models for science, ~20% "other".
- LLMs keep getting better, no publishing from the frontier labs, no big
  conceptual shifts as far as I can tell.
- Lots of hype around "virtual cells", there was even a [dedicated
  workshop](https://ai4d3.github.io/2025/index.html) for them. However,
  conceptually I don't think much changed: people are trying to fit models to
  gene expression data, sometimes other data too.
- Some trends in AI for science:
    - AI scientists, lots of exploring AI for literature search / reasoning /
      tool use
    - ML people recognizing that drug discovery is hard and can't be solved by
      making public benchmarks go up.
    - Slight preference towards fine-tuned open weight models instead of
      frontier models?
    - Lots of cool data development in structure-based drug design, eg CryoEM,
      more stuff using MD data
- Some talks I liked:
    - Eric Xing's talk about AIDO (AI digital organism, basically like virtual
      cell). Basically said "virtual cell won't be achieved by doing better on
      benchmarks every 3 months" and "we really need multi-modal data"
    - Yoshua Bengio's vision for a "Scientist AI" (basically a non-agentic
      system whose goal is to learn and say true things, you can query it to
      get actions but it doesn't actually have any goals itself).
- Best part of the conference was the people, good to meet people from other
  labs working on the same problems.
- I met a lot of BO researchers, and through conversations it finally became
  clear to me how I think the field of BO should re-orient itself so its work
  is more practical. I'll post a longer follow-up with my exact recommendations
  around the start of next year.
- PFNs (prior-fitted networks) are getting a lot of attention. I still have
  mixed feelings about them: their performance compared to exact Bayesian
  inference depends on generalization of the underlying transformer, especially
  in non-standard and misspecified settings. I'll see if people find successful
  use cases for them.

[^1]: but I was there for some nice company parties during the week 😀


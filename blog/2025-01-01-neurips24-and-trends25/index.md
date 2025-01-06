---
title: "Review of NeurIPS 2024 and predictions for ML in 2025"
date: 2025-01-01
tags:
    - machine learning
    - speculation
has_math: false
---

I was fortunate to attend NeurIPS 2024, arguably the largest and most
influential machine learning conference in the world (thanks Valence for
sponsoring my trip 🙏). In this post I will try to summarize what I learned at
NeurIPS, and cautiously make some predictions for the year ahead.

<!-- TEASER_END -->

First, some caveats:

- NeurIPS is an _enormous_ conference with many parallel tracks, thousands of
  papers and (probably) over 10k attendees. I did not (and could not have)
  witnessed the whole conference. My summary reflects the slice of the
  conference that I attended.
- I mostly attended AI for science talks/posters/workshops.
- Some of my time was spent trying to learn about topics which are relevant to
  projects at Valence which are not (currently) public. This post excludes such
  information.
- The insights on this page are (probably) not unique, and there are probably
  better NeurIPS summaries elsewhere.
- Not everything in the post is specific to NeurIPS, some is just general
  "stuff that happened in 2024"
- In retrospect, most of these predictions are basically "vibes" which are not
  falsifiable (eg "X will make 'significant' progress on Y"). This is because I
  had difficulties coming up with visible and tangible outputs of research
  progress (this is really hard). Ultimately I concluded that "vibes" are
  better than nothing. As a consequence, I solemnly swear to _not_
  retroactively point to this post and proclaim that I made prophetic
  predictions of the future. It helps that most of my predictions are probably
  not very controversial 😅
- Not all the prediction are carefully thought out (hence the "speculation"
  tag)

## AI scientists

**Status**: Although "AI for science" (ie AI for particular tasks in science)
has been a popular topic for a while, 2024 was the first year where a full "AI
scientist" hit the mainstream. [Sakana](https://sakana.ai/ai-scientist/) seemed
to be the first company to claim to have built an AI scientist, even though
[commentators suggested this was more hype than
substance](https://www.astralcodexten.com/p/sakana-strawberry-and-scary-ai).
Nonetheless, there were lots of "AI scientist" works at NeurIPS. The most
notable was the launch of [Lila](https://www.lila.ai/), who explicitly aim to
build an AI scientist. There is also
[FutureHouse](https://www.futurehouse.org/). There were also quite a few
posters that seemed to essentially "ask LLMs to propose an experiment and give
a step-by-step procedure for executing it" (although the capabilities
demonstrations all seemed underwhelming for me).

**Analysis**: I completely agree that "AI scientist" is a good direction to
pursue, not just to enhance scientific discovery but also for [safety
reasons](https://yoshuabengio.org/2024/02/26/towards-a-cautious-scientist-ai-with-convergent-safety-bounds/).
People seem to mostly be trying the "obvious" thing of LLM prompt engineering
and giving LLMs access to narrow tools (eg document retrieval or synthesis
planning). Although this has not produced impressive results in my opinion,
that is ok: big advancements take time to produce and perhaps even longer to
properly validate. I think the key question in this area is whether an "AI
scientist" is more than just the sum of the narrow tools which it has access
to.

**2025 predictions**

- There will be many more "AI scientist" announcements / papers. Almost all of
  them will be "all-hype-no-substance" and not worth spending much time on.
- The papers with substance will have a narrower scope (eg "AI scientist for
  designing better batteries"), including a narrow scope for the experiments
  available. However, there will be a decent number of such papers (probably
  ~10)
- Biggest advance over 2024 AI scientists will be in literature search. There
  will be a tool like FutureHouse's
  [PaperQA](https://github.com/Future-House/paper-qa) that is good enough to
  actually be worth using for developing research ideas, but _will not_ be a
  full substitute for literature searches.
- Somebody will start a proper study of whether an AI scientist can actually
  outperform a team of human scientists at a simple (but realistic) task.
  However, the study will not conclude in 2025 (maybe 2026)

## Large language models (LLMs)

**Status**: it should surprise exactly nobody that LLMs were an extremely hot
topic at NeurIPS. Despite huge advances in frontier models from
OpenAI/GDM/Anthropic, none of these were published at NeurIPS (following the
trend of frontier labs not publishing much).[^1] Countless posters analyzed
various aspects of frontier LLMs or did larger studies of smaller LLMs.

**Analysis**: very little here actually surprised me. Either I missed a lot (or
fell victim to confirmation bias), LLM progress is predictable, or I just have
a very good internal world model 🙃

- LLMs can still be easily jailbroken (offense seems dominant).
- Lots of engineering tricks can make transformer inference faster.
- LLMs are found to be mediocre at more and more tasks where "mediocre"
  performance is very impressive to achieve but not enough to actually replace
  existing workflows with LLMs (eg chemical synthesis planning). In the process
  of assessing this, more and more task-specific benchmarks have been created
  (which will be useful for assessing progress later on).
- On existing benchmarks, newer (and larger) LLMs perform better than older
  LLMs. Exactly what the "scaling hypothesis" predicts.
- Because frontier labs do not share their training data, studies generally
  cannot give a definitive answer to the question "did the model do well on
  task X because it (or something very similar) was present in its training
  data"?

**2025 predictions**

- Jail-breaking still unsolved (no "super" defenses)
- LLMs get a bit bigger and perform a bit better at most tasks
- Still no good way to answer "was it in the training data"
- LLMs in more applications providing "mundane utility"
- Frontier LLM labs still do not publish

## Foundation models for biology

**Status**: many labs seem to now be making an effort to produce foundation
models for biology, particularly using omics data.
[GenBio.ai](https://genbio.ai/) stood out to me in particular.

**Analysis**: this was not something I foresaw, but I guess it makes sense?
Omics data is pretty well-suited to transformers and with all the parallel
advances in transformers from NLP a serious "moonshot" attempt in biology seems
worth trying. One memorable takeaway from the "AI for new drug modalities"
workshop was that "not all foundation models are transformers, and not all
transformers are foundation models" (eg you can train a transformer on normal
tasks)

**2025 predictions**

- Lots more startups appear in this space
- Some kind of preliminary but non-trivial achievement from an industry lab

## Small molecule design

**Status**: still a big presence at NeurIPS. The overwhelming majority of
papers seemed to do 3D design of molecules with some kind of constraints (eg
fitting in a particular protein pocket or containing a certain fragment). No
discernible progress on creating better benchmarks in this area or addressing
the fact that real-world molecule design is not as simple as finding a molecule
with the right shape (eg there are other concerns like toxicity).

**Analysis**: my sense is that this field as stalled a little bit, at least
publicly. Yes we have 10000 variants of diffusion models, but are the models
useful? Unclear. I found this a bit disappointing (and I don't blame
researchers for this, I've also been thinking about this problem for a while
without producing a compelling solution).

**2025 predictions**

- Field still feels "stalled", though papers will still be published at NeurIPS
  \+ similar conferences
- More serious efforts in industry to deploy these techniques, with some
  success
- Best places to look for innovation will be in the methods section of
  Science/Nature-oriented papers
- At least one important innovation will _not_ be published (so I guess we
  won't know about it directly)

## Bayesian optimization (BO)

**Status**: not a ton of papers at NeurIPS, but there were some good ones, and
keep in mind that BO has never been hugely popular within the ML community.
Most work seems to be in approximations and applying BO to scenarios with
unusual restrictions. I particularly liked [a new way to set GP inducing points
for use in BO](https://arxiv.org/abs/2406.04308), [cost-aware BO using ideas
from Pandora's box](https://arxiv.org/abs/2406.20062), and Google's [Vizier GP
bandit algorithm](https://arxiv.org/abs/2408.11527)[^2].

However, from informal conversations it appears that many researchers derive
value from fairly "vanilla" BO in a variety of domains, which is encouraging.

**Analysis**: my sense is that BO has a lot of untapped application potential,
especially in areas outside of A/B testing and hyperparameter optimization.
There is still a lot of room to develop BO-like methods for tasks outside of
single-objective optimization, and analyzing the effect of approximate
inference.

**2025 predictions**

- More and more companies will derive "mundane utility" from BO
- People compare BO to LLMs for decision-making. These comparisons will not be
  "fair" in that they will use a pretty vanilla BO setup without much tuning.
- Despite a lot of potential, only a handful of groups will continue to do
  serious BO work (probably mostly the same people as before)

## General AI-powered productivity tools

**Status**: as far as I know there were no legible artifacts about this from
the conference (eg posters, recorded talks). However, from conversations with
other researchers I found more and more people getting value from
general-purpose AI productivity tools. People ask questions to ChatGPT / other
foundation models. People use co-pilot + similar tools when writing code.
People use ChatGPT to help proofread papers.

**Analysis**: these tools must be more useful than before. My sense is that if
you don't use an LLM tool at least once per day as part of your work then you
aren't using LLMs enough. I think I should personally use LLMs more.

**2025 predictions**

- More researchers use LLM tools
- More niche tools that save time (for example, something like really reliable
  sorting of priority emails would save a lot of email time)
- Range of tasks where LLMs are useful increases

## AI safety / alignment

**Status**: lots of safety-relevant posters, talks, and workshops. A lot of
"analysis" work, but nothing that comes close to "solving" safety/alignment.

**Analysis**: safety is becoming a lot more mainstream, which is encouraging.
I'm not seeing much of the "alignment research is bad because it distracts from
present issues" argument. No surprise that it isn't solved.

**2025 predictions**

- Trends continue: safety becomes more mainstream as LLMs become more powerful,
  and we still do not "solve" safety because it is an immensely hard problem

## Conclusion

Overall, ML has grown bigger every year for the past 10 years, and 2024 was no
exception. I don't see why 2025 will be an exception either. Let's see how
things play out!


[^1]: There were of course many people from these frontier labs in attendance.

[^2]: NOTE: not presented at NeurIPS. I wrote a [previous blog post](/blog/2024-10-13-vizier-bayesopt/) about it.

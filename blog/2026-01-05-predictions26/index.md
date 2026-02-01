---
title: "Predictions for ML/AI in 2026 (and 2025 predictions re-visited)."
date: 2026-01-05T01:00Z
tags:
    - machine learning
    - speculation
    - _recent-highlight
has_math: false
---

Last year [I made a bunch of predictions about
ML](/blog/2025-01-01-neurips24-and-trends25/), and since 2025 is over it's time
to grade myself and repeat this exercise.

<!-- TEASER_END -->

This will be a lower effort version than last year's: partly because AI is
growing and I don't think I'm doing a good job keeping track of it, partly
because a lot of progress is happening behind closed doors of frontier labs (so
less info is available to me as an outsider), and partly because other people
have already made a bunch of good predictions.[^recs] Therefore my predictions
are neither very bold nor very original.

[^recs]: I'll highlight predictions from the [State of AI report](https://www.stateof.ai/2025-report-launch).

## Grading my 2025 predictions (quick version)

My 2025 predictions are from [this blog
post](/blog/2025-01-01-neurips24-and-trends25/). I'll quickly give each one a
score (without rigorous research, apologies for being a bit sloppy).

### AI scientist predictions

My original predictions:

> - There will be many more "AI scientist" announcements / papers. Almost all of
>   them will be "all-hype-no-substance" and not worth spending much time on.
> - The papers with substance will have a narrower scope (eg "AI scientist for
>   designing better batteries"), including a narrow scope for the experiments
>   available. However, there will be a decent number of such papers (probably
>   ~10)
> - Biggest advance over 2024 AI scientists will be in literature search. There
>   will be a tool like FutureHouse's
>   [PaperQA](https://github.com/Future-House/paper-qa) that is good enough to
>   actually be worth using for developing research ideas, but _will not_ be a
>   full substitute for literature searches.
> - Somebody will start a proper study of whether an AI scientist can actually
>   outperform a team of human scientists at a simple (but realistic) task.
>   However, the study will not conclude in 2025 (maybe 2026)

Evaluation:

- There were a _huge number_ of AI scientist papers (many of which were just
  "hype" in my opinion).
- Many of the ones I liked more did focus on a particular area, although
  [Kosmos](https://edisonscientific.com/articles/announcing-kosmos) defied my
  expectations and did interesting work on a wide scope of problems.
- Literature search tools _did_ advance a lot (eg Deep Research tools from
  OpenAI and Google). However, these tools aren't perfect and seem to generate
  a lot of "slop" (not too much to be useful, but too much to be a perfect
  substitute for human research).
- No idea whether a study was done to compare human scientists an AI scientists
  on non-trivial tasks. I know some papers have compared humans and AI on
  hypothesis generation. I'll look out for this in 2026.

I'll give myself 8/10 here.

### LLMs

2025 predictions:

> - LLMs can still be easily jailbroken (offense seems dominant).
> - Lots of engineering tricks can make transformer inference faster.
> - LLMs are found to be mediocre at more and more tasks where "mediocre"
>   performance is very impressive to achieve but not enough to actually replace
>   existing workflows with LLMs (eg chemical synthesis planning). In the process
>   of assessing this, more and more task-specific benchmarks have been created
>   (which will be useful for assessing progress later on).
> - On existing benchmarks, newer (and larger) LLMs perform better than older
>   LLMs. Exactly what the "scaling hypothesis" predicts.
> - Because frontier labs do not share their training data, studies generally
>   cannot give a definitive answer to the question "did the model do well on
>   task X because it (or something very similar) was present in its training
>   data"?

I think these all hold up, although these were not terribly difficult or
original predictions to make.

### Foundation models for biology

2025 predictions:

> - Lots more startups appear in this space
> - Some kind of preliminary but non-trivial achievement from an industry lab

Lots of people are doing "virtual cells" (including
[Valence](https://arxiv.org/abs/2505.14613) 💪), not sure how many are startups
though. It feels like there was no "non-trivial achievement" (at least none
that I can remember now). I'll give myself 3/10 here.

### Small molecule design

2025 predictions:

> - Field still feels "stalled", though papers will still be published at NeurIPS
>   \+ similar conferences
> - More serious efforts in industry to deploy these techniques, with some
>   success
> - Best places to look for innovation will be in the methods section of
>   Science/Nature-oriented papers
> - At least one important innovation will _not_ be published (so I guess we
>   won't know about it directly)

Analysis: most of these predictions were not concrete and falsifiable, but
overall I agree with the predictions. I'll subjectively give myself 7/10
(noting of course that the last prediction is completely unverifiable).

### Bayesian optimization

2025 predictions:

> - More and more companies will derive "mundane utility" from BO
> - People compare BO to LLMs for decision-making. These comparisons will not be
>   "fair" in that they will use a pretty vanilla BO setup without much tuning.
> - Despite a lot of potential, only a handful of groups will continue to do
>   serious BO work (probably mostly the same people as before)

Analysis: overall seems true. Probably LLMs are being chosen over BO for
slightly more tasks than I expected, so I'll give myself 6/10.

### General AI-powered productivity tools

2025 predictions:

> - More researchers use LLM tools
> - More niche tools that save time (for example, something like really reliable
>   sorting of priority emails would save a lot of email time)
> - Range of tasks where LLMs are useful increases

Analysis: these were fairly easy predictions to make. Definitely more
researchers use LLM tools. Niche tools are definitely there, but it feels like
we got "general" tools that feed context into the frontier models (eg cursor)
instead of "niche" tools. LLMs clearly just got more useful. I'll give myself
6/10.

### AI safety / alignment

2025 prediction (just 1):

> - Trends continue: safety becomes more mainstream as LLMs become more powerful,
>   and we still do not "solve" safety because it is an immensely hard problem

Analysis: seems true, 10/10.

## Quick 2026 predictions

For now I will just make predictions on the level of increase (⬆️) or decrease
(⬇️) in importance / use / prominence of research directions or sub-fields.

- **AI scientists**: ⬆️
- **AI drug discovery**: ⬆️
- **LLMs**: ⬆️ (but be on par with how important the AI community thinks they
  will be, which is _very_ important)
- **Bayesian optimization**: ⬇️ (unfortunately 😢, maybe with the exception of a
  few sub fields)
- **Virtual cells / foundation models for biology**: ⬆️
- **AI increasing everyday productivity** ⬆️

Mostly these predictions are just "current trends will continue", so they
aren't very original.


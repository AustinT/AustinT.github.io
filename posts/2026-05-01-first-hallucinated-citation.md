---
title: 'First time encountering a hallucinated citation of my paper.'
date: 2026-05-01T08:00Z
tags:
    - book
    - drug discovery
has_math: false
---

I recently ran an LLM deep research query about large matrices of Tanimoto
coefficients,[^why] and one of its references was the paper "Bandwidth
adjustable Tanimoto kernel: a smooth alternative to the Gaussian kernel"
(<https://doi.org/10.1007/s41237-026-00296-7>). Skimming this paper, I found a
citation whose title and publication venue matched my own paper, but with a
completely different author list:

<!-- TEASER_END -->

[^why]: One might encounter these when deploying Tanimoto Kernel Gaussian Processes on large datasets.

> Krishnapriyan A, Schwaller P, Dral PO, Galuba W, Hegde C (2020) Tanimoto
> random features for scalable molecular machine learning. In: Advances in
> Neural Information Processing Systems (NeurIPS), volume 33, pp. 12233–12245

As far as I can tell, this is a completely hallucinated citation:

- The authors are mostly real ML researchers who have (mostly) done chemistry-related research.
    - [Aditi Krishnapriyan](https://scholar.google.com/citations?user=7HoFN1wAAAAJ): AI for physics.
    - [Philippe Schwaller](https://scholar.google.com/citations?user=Tz0I4ywAAAAJ): ML for chemistry.
    - [Pavlo O. Dral](https://scholar.google.com/citations?hl=en&user=TPjal54AAAAJ): on the QM9 dataset
    - [Wojciech Galuba](https://scholar.google.com/citations?hl=en&user=jyaTX64AAAAJ): the odd one out, seems to mostly have done computer vision.
    - I can't find a profile for "Hedge C" though
- The NeurIPS 2020 proceedings ([link](https://papers.nips.cc/paper_files/paper/2020)) has no paper with "Tanimoto" in the title.
- Googling this paper title / author list returns no results that match.

On the other hand, _I_ have a paper called "Tanimoto random features for
scalable molecular machine learning" from my PhD:

- arXiv: <https://arxiv.org/abs/2306.14809>
- OpenReview: <https://openreview.net/forum?id=MV0INFAKGq>
- NeurIPS 2023 proceedings: <https://proceedings.neurips.cc/paper_files/paper/2023/hash/6a69d44b3386e50c06f7107ef4f29302-Abstract-Conference.html>

I see no other explanation than an LLM hallucination: my paper seems to be the
only academic article out there with this title. I see no plausible way that a
real person who looked at the paper would get the title and venue right, but
mess up the author list and year (it was also wrongly attributed in the main
text). However, it seems like a mistake an LLM would make: recalling the title,
then filling in a plausible set of authors who are in ML.

I view this partly as an accomplishment- the LLMs have clearly internalized the
existence of my paper and its core idea, without needing to rely on RAG. The
offending paper does vaguely describe my papers' contribution correctly, so it
hasn't _completely_ misinterpreted it (although admittedly the contribution is
basically in the title).

The rest of the offending paper is a bit confusing: aside from the hallucinated
references, it also contains the phrase "Table??" 4 times, suggesting a LaTeX
compilation error. I almost think this is too _bad_ to have been done by AI- if
anything AI seems overly eager to always lint and recompile things. I wonder
whether the authors just used AI for their references, or are just bad at using
AI... 🤔

Nonetheless, this is ultimately a sad state for science to be in. The journal
Behaviormetrika is apparently an established an reputable journal, so I'm
surprised this slipped through...


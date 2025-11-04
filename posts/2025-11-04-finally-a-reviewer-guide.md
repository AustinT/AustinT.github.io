---
title: "Finally, an ML conference review guide!"
date: 2025-11-04
tags:
    - machine learning
    - peer review
has_math: false
---

ICLR 2026 released a detailed review guide as part of its review process
([link](https://iclr.cc/Conferences/2026/ReviewerGuide)). Let's analyze it!

<!-- TEASER_END -->

Here is a copy/paste of the first bit of the guide (copied 2025-11-04):

> 1. Read the paper: It’s important to carefully read through the entire paper and to look up any related work and citations that will help you comprehensively evaluate it. Be sure to give yourself sufficient time for this step.
> 1. While reading, consider the following:
>     1. Objective of the work: What is the goal of the paper? Is it to better address a known application or problem, draw attention to a new application or problem, or to introduce and/or explain a new theoretical finding? A combination of these? Different objectives will require different considerations as to potential value and impact.
>     1. Strong points: is the submission clear, technically correct, experimentally rigorous, reproducible, does it present novel findings (e.g. theoretically, algorithmically, etc.)?
>     1. Weak points: is it weak in any of the aspects listed in b.?
>     Be mindful of potential biases and try to be open-minded about the value and interest a paper can hold for the entire ICLR community, even if it may not be very interesting for you.
> 1. Answer four key questions for yourself to make a recommendation to Accept or Reject: 
>     1. What is the specific question and/or problem tackled by the paper?
>     1. Is the approach well motivated, including being well-placed in the literature?
>     1. Does the paper support the claims? This includes determining if results, whether theoretical or empirical, are correct and if they are scientifically rigorous.
>     1. What is the significance of the work? Does it contribute new knowledge and sufficient value to the community? Note, this does not necessarily require state-of-the-art results. Submissions bring value to the ICLR community when they convincingly demonstrate new, relevant, impactful knowledge (incl., empirical, theoretical, for practitioners, etc).
> 1. Write and submit your initial review, organizing it as follows: 
>     1. Summarize what the paper claims to contribute. Be positive and constructive.
>     1. List strong and weak points of the paper. Be as comprehensive as possible.
>     1. Clearly state your initial recommendation (accept or reject) with one or two key reasons for this choice.
>     1. Provide supporting arguments for your recommendation.
>     1. Ask questions you would like answered by the authors to help you clarify your understanding of the paper and provide the additional evidence you need to be confident in your assessment. 
>     1. Provide additional feedback with the aim to improve the paper. Make it clear that these points are here to help, and not necessarily part of your decision assessment.

## Analysis

As I mentioned in a [previous post](/blog/2025-06-22-ml-conference-review-guide/),
my internal review criteria is essentially "correct AND (result OR idea).
How does this compare?

Overall I think it is compatible. ICLR's guide emphasizes understanding the
goal (aka objective) of the paper, then analyzing it with this goal in mind. I
don't explicitly have that as a criteria, but I think it is implicit in the
paper containing a result or an idea (presumably the goal of the paper is to
present that result or idea). Step 3.3 seems essentially the same as my
"correctness" criteria, and 3.4 (significance) is what I would call "result OR
idea".

## "Motivation"

One thing they highlight which I don't highlight is motivation and placement in
the literature (3.2). This is an interesting one. I feel like a lot of
empirical papers propose an interesting idea, but motivate it poorly. Here is a
hypothetical example, blending together maybe ~20 papers I've read over the
years:

> Drug discovery is an important problem [1-25], lots of people have tried ML
> for it [26-100]. Unfortunately, ML works best when you have a lot of data
> [100-200] and we don't have a lot of data. Also, scientists know a lot of
> stuff and it would be useful to put it into models [200-500]. Anyway, here is
> our new molecular property prediction method which blends together 3
> different model architectures and doesn't actually address these problems.

Essentially they point to a generic series of problems in the field, then
present their model, which does not actually address most of these points.
Usually I just overlook this, but perhaps I shouldn't? Poor introductions like
these definitely make papers more difficult to read.

## Conclusion

Overall good guide, I'm happy they provided this, and it encouraged me to call
out poor motivation and contextualization more than I do already.

---
title: "Stock responses about statistical significance for reviewing machine learning papers"
date: 2025-02-11
tags:
    - machine learning
    - peer review
has_math: false
---

So many ML papers contain tables like

|Method|Score(↑)|
|---|----|
|Baseline 1|49.9%|
|Baseline 2|49.8%|
|Baseline 3|50.0%|
|**Our super fancy SOTA method**|**50.1%**|

then say "results on the benchmark show that our method is state-of-the-art for task X."

<!-- TEASER_END -->

When I encounter this as a ML paper reviewer, my first response is usually
something to the effect of "The entries in your table are random and the
differences are low, I think you need error bars and a statistical test result
to support claims about significance". Occasionally the authors do follow up
with test results which show significance, but more often they do not. I've
seen many different reasons. Here I will go through a bunch of examples and
give my recommendations for what to say to authors.

## Author responses and my suggested follow up responses

### "Clearly not significant"

Authors:

> We are happy to provided error bars. Please see updated table. Error bars are computed over 3 samples.
> 
> |Method|Score(↑)|
> |---|----|
> |Baseline 1|49.9±10%|
> |Baseline 2|49.8±10%|
> |Baseline 3|50.0±10%|
> |**Our super fancy SOTA method**|**50.1±10%**|

(Translation: their results are very clearly not statistically significant)

**My suggested response (honest)**: this is obviously not significant you
idiots.

**My suggested response (diplomatic)**: I don't think these results support the
claim of "state-of-the-art performance over baselines". The error bars suggest
that the result is not statistically significant (although it would be
appreciated if the authors could provide the results of a statistical test to
confirm this).

### EXPENSIVE experiments

Authors:

> My dear reviewer, you don't understand: my experiments are ExPeNsIvE, I
> cannot simply ReRuN tHeM.

(Translation: they cannot gather more observations, and want reviewers to just
say "ah I see, never mind then, your results are great")

**My suggested response (honest)**: ... excuse me, how exactly is this an
argument to not think about statistical significance?

**My suggested response (diplomatic)**: I understand that experiments are
expensive, but in situations where statistical significance cannot be tested
with repeat experiments, I think it would be appropriate to revise claims of
"state-of-the-art performance" to just be "competitive performance".

### The poor academic

Authors:

>Please sir, I'm a poor academic with half a GPU. I'd be happy to re-run them
but it would take 6 months and we only have 1 week for the rebuttal.

**My suggested response (honest)**: I'm truly sorry for you, but this isn't
really my problem? I'm just the reviewer and it's my job to hold this work to
actual scrutiny!

**My suggested response (diplomatic)**: I understand that the conference review
timeline does not leave time to run additional experiments. Given that, I think
the appropriate action is to revise the claims about "state-of-the-art
performance". If you would like to keep these claims, I still believe
additional experiments are required to support them.

### Appeal to tradition

Authors:

> We totally agree this is bad practice, but we were merely following the
> experimental procedure of the previous paper.

(Translation: other people did this and that makes it ok)

**My suggested response (honest)**: Gah, I do feel this one. Seeing bad
practice get published makes you learn bad practices. Also, even if you know it
is bad practice, it does make developing new methods easier if you build on
code from previous work. That all being said, I cannot with good conscience let
this stand.

**My suggested response (diplomatic)**: (basically like above but said less
informally)

### You asked for a test? I'LL GIVE YOU A TEST!

Authors:

> We re-ran experiments and performed the "5-sided bias-corrected Smith-Li
> non-parametric test" and achieved a significance value of `p=1e-7`

(Translation: we tried every possible statistical test until we got a good
significance result)

**My suggested response (honest)**: I wish I knew enough about statistical
testing to say what's wrong here, but I just find this very suspicious.

**My suggested response (diplomatic)**: Thank you for performing this test. Can
you please explain why the above test was used instead of a more common test
like a t-test? If possible, could the authors also provide the results of a
t-test (even if they think it is not the most appropriate test)?

## Conclusions

Paper authors: if you can't give a 1 minute explanation of why statistical
tests are important in machine learning, you should not be doing machine
learning research. Drop whatever you are doing and spend 1h reading about
statistical tests. The basic concepts are not particularly difficult, and you
don't need to be an expert (I'm certainly not). You can come back to your
normal research after 1h.

Paper reviewers: please don't let these bad practices slide through the review
process without criticism! It really isn't difficult to ask for significance
tests, or push back against authors (I hope my responses help a bit with this).
However, please don't default to thinking "significant results are needed for
me to accept the paper". There are lots of contributions which are interesting,
even if they don't achieve statistically significant results.[^examples]
Notice that most of my responses are not "aha, found a flaw, your paper gets
rejected"- I usually just suggest revising the claims (although with the
revised claims that may be a good reason to reject the paper).

[^examples]: Example include methods which are faster/cheaper but give the same performance, improving a method which usually underperforms (even if the improved version is still beaten by another method), or simplified methods (even if the simplification causes a slight performance drop).

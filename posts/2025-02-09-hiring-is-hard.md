---
title: "Hiring is hard: why good applicants without connections can get overlooked."
date: 2025-02-09
tags:
    - employment
has_math: false
---

Knowing people is a great way to get hired. Nepotism is one obvious explanation
(aka people hire you because they like you, or to gain favors from people who
like you). I (along with most other people) think that nepotism is bad: it's
unfair, and gives jobs to people who are probably not that good at them.
However, it is a mistake to think that nepotism is the only reason why people
who are known get hired, and that this practice is always bad. Some better
reasons are:

<!-- TEASER_END -->


1. Very high confidence in a person's skills (eg "I sat beside this person
   every day in graduate school, they always helped me with X, I am 99.9%
   confident that if we hire them they will be great at X").
2. Soft skills or interpersonal factors which can be hard to assess in an
   interview (eg "This person is not a jerk and will be pleasant to work with"
   or "This person is insanely dedicated").
3. In very niche fields often all the best people _will_ be known to you (eg
   "Only 1 competitor company and 1 university develop super niche technology
   X, and I (hiring manager) know everybody at both places").
4. Many companies' hiring systems are inadequate to reliably sift out good
   applicants whose names are not already on a hiring list (eg "None of the
   applicants we looked at seemed as good as Bob, so let's hire Bob").

I feel like I have seen a decent amount of content about points 1-3 before, but
not so much on point 4, so that is what the rest of this post will be about.


<div class="alert alert-danger">
To be clear, this post <b>should not</b> be interpreted as a criticism of my employer (Valence).
As I explain below, the "inadequacy" of hiring systems is mainly about hiring being hard.
If you are skilled and interested in AI for drug discovery, you should absolutely apply to Valence
(but I encourage you to follow the advice at the end of this post).
</div>

## The "inadequacy" of hiring systems is largely just hiring being hard

Many job postings have the following properties:

1. They describe a very specialized job with a broad range of tasks and a wide
   range of necessary (and preferred) skills. These are difficult to summarize
   externally (ie on the job posting) and internally (eg what a hiring manager
   might communicate to HR).
2. They attract a _very large_ number of applicants. A desirable role at a
   large well-known company (think "software engineer at Meta-soft") could
   plausibly attract 10k-100k applicants.
3. They compel many people who have no realistic chance of being hired to apply
   anyway (think "I am 25% through an intro python course and have no other
   programming experience" for a senior software engineer role).

(2) means that even _glancing_ at every application requires a substantial
amount of time (days, weeks, or even months). The hiring manager will probably
_not_ be able to look through all applications. (3) creates the temptation to
automate filtering because it is usually very obvious when somebody does not
have skills relevant for a job, and often a large fraction of applicants are
clearly underqualified. Unfortunately, (1) makes it difficult to do this
automation well (or outsource it to a different team, such as HR).

## Keywords are a poor stopgap, but surprisingly difficult to avoid

From what I have heard anecdotally, the overwhelming majority of application
filtering systems rely on keywords. Usually these are skills from the job
description (eg "python", "cell culturing"), but can also be about degrees
received, universities attended, previous work experience, etc. Of course,
keyword searches have many opportunities for false negatives:

- Hard to specify all forms of a word (eg "Amazon web services" or "AWS",
  "scikit-learn" or "sklearn", "ML" or "machine learning" or "AI" or
  "artificial intelligence").
- Not everybody puts keywords on their CV, even if they have the skills (eg if
  I have a publication whose code uses libraries X/Y/Z, I might not list X/Y/Z
  on my resume).
- Things like line breaks or hyphenation make it difficult to automatically say
  whether a PDF document actually contains a certain phrase (eg "Mach-ine
  learning" printed due to a line break).

Also, nobody is in a great position to actually design keyword searches.
Managers understand the job requirements but are probably not used to thinking
in terms of keywords (at least relative to HR or recruiters). HR/recruiters
usually don't understand the job requirements very well.

However, I actually think it's harder to do better than keywords. You can't
easily search for vague things like "does this person have a serious research
background",[^vague] even though this would be helpful. You _can_ ask
applicants more detailed application questions (eg "why are you qualified for
the job", "please input every publication into this form"), but this makes
applications harder to fill out, and the sheer number of applicants might still
mean that a human can't look through every single response.

[^vague]: At least until the advent of LLMs. More on this below.

## An aside: LLMs to the rescue?

When writing the previous section, I can't help think that LLMs are very
suitable for improving this process. Yes LLMs have issues with bias / fairness
/ hallucinations, but nonetheless it would be really helpful to compare all of
a candidate's application text to a given prompt. If this isn't already a
startup then I really think it should be one.

## Takeaways

For applicants, I think:

- Put as many keywords as possible into your CV
- Email (potential) hiring managers directly so they are aware of your
  application and won't miss it. NOTE: please only do this if you are actually
  a good fit for the role, otherwise it is just annoying.

For employers:

- Do your best to write good job descriptions
- If you need to use keyword searches, do this very carefully
- Don't rely on HR to do a good keyword search for you (they are probably not
  very familiar with what skills the job actually requires)

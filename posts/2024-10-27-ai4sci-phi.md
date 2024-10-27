---
title: "Advice for applying for a PhD in AI for science in 2024"
date: 2024-10-27
tags:
    - PhD
    - speculation
has_math: false
---

With the immense growth of AI for science (AI4sci for brevity), I imagine many
younger students are considering applying for PhDs in AI for science in this
application cycle. This post is my attempt to turn my 5 years of experience in
AI4sci into actionable advice for prospective PhD students.

<!-- TEASER_END -->

<div class="alert alert-success">
NOTE: AI is a quickly-moving field
and the advice in this post may quickly become outdated.
If you are reading this more than 1 year since publication,
you may want to disregard a lot of this post's content.
</div>

Let me start with a big disclaimer: the advice in this post might not be right
for you. A PhD is a very individual, and what worked for me might not work for
you. I also do not (and really _cannot_) have perfect knowledge of a field as
broad as AI4sci. If your interest is far away from my core experience of "AI
for drug discovery" (eg AI for paleontology), my advice is probably less
relevant.

## Advice 1) Look at general advice for applying to PhDs

Fundamentally, a PhD in AI4sci is not that different from a PhD in any other
field. Yes, the job prospects and funding in AI4sci is better than for
comparative literature, but the experience itself is surprisingly similar: you
spent years studying a niche topic, usually alone. Therefore, I recommend you
search for "general" advice about applying for PhD programs, including the
question of whether you should apply at all. In my opinion, the top 3 pieces of
"general" advice to consider are:

1. Learn how busy your supervisor will be (eg will they meet you 1h per week
   and discuss your research with you in detail or will they meet you 30min
   every 3 months and give high-level advice).
2. Try to learn whether your supervisor is a good person to work with. Toxic,
   mean, exploitative, or chaotically disorganized people are surprisingly
   common in academia. Either avoid them or be clear with yourself about what
   you are signing up for.
3. Try to understand the overall "status" of the field you will enter. Is it
   growing, stagnant, or dying? Is there a lot of interest from industry? This
   will significantly influence your post-PhD career options.

I may write a blog post later on with more advice. Otherwise, there is lots of
stuff available on the internet. I personally found
<https://shouldigetaphd.com/> helpful.

## Advice 2) consider the department

AI4sci is an interdisciplinary topic which is usually researched in one of two
departments:

1. A _science_ department (eg chemistry, physics)
2. A _"machine learning"_ (ML) department (eg engineeering, computer science,
   math)

The department you belong to can have a surprisingly large impact on what
skills you will learn in your PhD. In a science department you will learn more
about science, and in an ML department you will learn more about ML. This is
because:

- Your supervisor's training will usually match the department's focus, and
  they will give the best feedback on the subjects where they have training.
- Most colleagues (eg postdocs, fellow PhD students, and other people in your
  building) will also have undergraduate/graduate training in the subject
  matching the department name.
- The seminars and reading groups hosted by your department will skew towards
  the department's core subject.

Overall, this means that your training will likely be _imbalanced_, and you
will either exit the PhD as "more of a scientist" or "more of an ML person". 
Think about what you want to become. If you don't know what you would want to become, here are
my pros/cons for each option:

### Science-first

Pros:

- You learn what problems are important
- You learn what solving the problem might actually look like
- You learn what the data means and what data is out there that can be used

Cons:

- You will learn less about the ML methods themselves
- Specializing in one discipline, you might not be exposed to other disciplines
  which use similar methodology

### ML first

Pros:

- You learn a lot of methodology
- You naturally get exposed to problems in a lot of different disciplines
- Easier to transition to "ML for something else" if you don't like the
  scientific application from your PhD

Cons:

- You don't learn much about one particular problem
- You don't tend to see how non-ML solutions are used. Some people exit ML PhDs
  with one "hammer" that they want to use for every "nail"

### Mini-conclusion

I did a science undergraduate degree so I felt that I would benefit more from
learning about ML methods rather than focusing more on chemistry/materials. In
hindsight I think that was the right decision for me, but it is probably not
the right path for everybody.

My sense is that, overall, going for a science-first approach is the better
option now. A lot of ML researchers are transitioning to AI4sci since it is one
of the few areas where LLMs do not completely dominate (at least so far). With
a lot more competition from the ML side, you might have better chances
specializing in the problem itself. This is just speculation though, and
"average" advice as best. As I write below in point 4), you should consider
specific sub-fields individually rather than "AI4sci" as a whole.

## Advice 3) who will you learn from in the research group

Ideally this would be your supervisor. However, in general, the more successful
a professor is, the more responsibilities they take on, resulting in you
getting less feedback. So, if you have a professor in mind, try to get a sense
of how much time they have. If they have little time, are there postdocs or
other PhD students you can learn from? This may sound like second-class
supervision, but I think that learning from a good postdoc can often be a lot
better than learning from a good supervisor, especially for low-level technical
challenges. For example, a famous professor is probably not going to know much
about how to get `pytorch` code to run efficiently, but a good postdoc in ML
would.

Secondly, in addition to _who_ you will learn from, think about _what_ you
could learn from them. Does their expertise match your interests? If not, you
might not learn as much as you would think. If, for example, you want to use
language models for drug design and join a high-profile machine learning group
specializing in computer vision, they might not be able to teach you many
relevant skills for that project.

## Advice 4) think about the sub-field

AI4sci is a unified term for many different problems. Not all of these problems
are very well-suited to studying in a PhD. To give some examples:

- "Unifying quantum mechanics and general relativity with AI"- seems hard, and
  it's not clear exactly how AI would help.
- "Predicting chemical reaction yields with AI"- solving this problem would be
  super impactful, but there is very little public data for this which makes
  progress difficult.

Therefore, I recommend trying to form an opinion on how promising your
particular AI4sci topic is. I will give my slightly-informed, weakly-held
opinions on a few problems / sub-fields below.

### LLMs for science

This is a hugely popular topic, but everybody seems to be working on it
(including lots of companies and startups). Probably very competitive, so
harder to do good research in this space.

### Protein design / structure-based drug design

Arguably the second most popular topic after LLMs, this space is also very
competitive, and is also filled with a lot of companies. My guess is that it is
over-saturated. Unless you plan on joining a lab with really good resources in
this space (eg David Baker's lab at UW), I recommend trying to focus more on
_analyzing and understanding_ models rather than trying to develop the latest
and best protein generation model.

### ML for weather prediction

This space is growing quickly but companies like DeepMind and Microsoft are
targeting this problem. You will most likely not have the compute resources to
compete with them as a PhD student. If you want to go into the field, maybe
focus more on _analyzing_ models rather than training the best ones.

### AI for small-molecule drug discovery

This is most closely related to what I did during my PhD. My overall impression
is that we have done all that we can with public data, and that the best way to
improve is to get more data. This is a lot of the reason why I took an industry
position at Valence Labs. If you want to do work in this area try to join a lab
with its own data source.

### AI for molecular force fields

Another very popular topic. I am less certain what the public data is like for
this. My sense is that there is still a lot of work left to be done in
academia, so this is probably a decent problem to work on during one's PhD.
However, it seems to have become clear that just throwing deep learning at this
problem has not solved it. To have a decent chance at making progress you
probably need an understanding of the physics and the various data sources that
are available. Perhaps this problem is best addressed in a physics group?

## Summary

Essentially, my advice is:

- Do a lot of searching about applying for PhDs in general
- Think about which department you want to be based in: a science department or
  an ML department
- Think about who you would learn from in your research group
- Think about the potential of AI4sci in the specific sub-field you are
  thinking of entering, instead of just AI4sci as a whole

Good luck! If you have questions or comments, please feel free to email me (or
contact me via Twitter).

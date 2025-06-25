---
title: "Conceptual confusion about desirable outputs of reaction prediction models."
date: 2025-03-27
tags:
    - retrosynthesis
    - chemistry
    - machine learning
    - speculation
has_math: false
---

In the literature about machine learning for retrosynthesis, one line of work
tries to predict chemical reactions, either in the _forward direction_ (ie what
products will A + B form) or in the _backward direction_ (ie what reactants
could react to produce molecule C). Such models are often trained on datasets
of known reactions like Pistachio or USPTO, with the hope of generalizing to
new "correct" reactions. However, this formulation of the problem overlooks a
lot of subtleties about what makes a reaction "correct". In this post I will
present a more nuanced mental model which (hopefully) clarifies some
ambiguities.

<!-- TEASER_END -->

<div class="alert alert-info">
This is a "quickpost": a post which I have tried to write quickly, without very much editing/polishing.
For more details on quickposts, see
<a href="/blog/2025-02-11-lowering-quality/">this blog post</a>.
</div>

## My model of correctness

Importantly (but somewhat pedantically), there is arguably no such thing as an
"absolutely correct" reaction prediction in ML. Because conditions and minor
products are not reported, ML reaction predictions are _underspecified_ and
therefore somewhat "unfalsifiable".[^unfalsifiable] That aside, there are at
least 3 separate kinds of reaction correctness:

[^unfalsifiable]: As in, there is no experiment that could falsify the predictions, since, for example, a failed reaction at one set of reaction conditions does not preclude the reaction succeeding for another set of conditions.

1. **Feasibility**: the reaction _could_ succeed (under _some_ set of
   conditions and other minor products).
2. **Desirability**: the reaction is one you would actually want to perform.
3. **Reasonability**: the reaction is a good choice among comparable
   alternatives.

These criteria may not agree. For example, the reaction `Pb -> Au` (lead
becomes gold) is highly desirable and very reasonable over alternative
reactions like `Ag -> Au` (silver to gold), but is not _feasible_. The reaction
`H2 + O2 -> H2O` is both feasible and reasonable (compared with other ways of
making water), but not very desirable if your goal is small molecule drug
discovery (because you are interested in different reactions). The reaction
`C6H6 + O2 -> CO2 + H2O` (combustion of benzene) is feasible and desirable if
your goal is to make carbon dioxide, but if carbon dioxide is your goal then
burning methane (`CH4 + O2 -> CO2 + H2O`) is probably cheaper and easier,
making this not the most reasonable choice.

Feasibility is essentially a consequence of physics and is arguably universal.
However, desirability and reasonability are both highly dependent on
"contextual factors", for example:

- Which reactions are "desirable" for a synthesis routes depends on the set of
  starting molecules that you have, or the kinds of molecules you want to make.
- Which reactions are "reasonable" depends on what equipment and inventory you
  have. It may normally be preferable to use an inexpensive reactant over an
  expensive one, but if you have already purchased a jar of the expensive
  reactant then the marginal cost of using it is effectively zero.

## Why is this important?

Reactions from datasets like USPTO and Pistachio tend to satisfy all 3 notions
of correctness:

- They should be feasible, since they are extracted from papers and patents and
  were therefore successfully performed once.[^errors]
- Desirable, since somebody chose to do them for something.
- Reasonable, since they were chosen over other alternatives.

[^errors]: Except for many errors / "annotation quirks" in these datasets.

Because of this, I think it is easy for people in ML to conflate these kinds of
correctness or simply not care about the distinction between them. However,
when actually applying these methods, one's "contextual factors" can be a lot
different than the contextual factors used to generate these datasets, which
can cause reaction models to fail in "unexpected"[^unexpected] ways, for
example:

[^unexpected]: These failures are unexpected _if_ you do not distinguish between these different notions of correctness.

- A model may not output reactions which use the reagents you have in stock
  (because how would the model know what you have in stock).
- A model may not distinguish between cheap and expensive reactants because
  patents may preferentially show routes with expensive alternatives (since
  patents try to make the invention hard to replicate).

## The way forward

Practitioners want reaction models which output feasible reactions, and
desirable/reasonable reactions according to _their own_ contextual factors.
Therefore, they should rely on training datasets as correctness labels only
insofar as the contextual factors of the training datasets match their own.
Unfortunately, _I am not sure how to do this more precisely._ Probably you
would need some kind of additional training signal about "contextual factors"
besides the public datasets, or you would need to add your own training data
into the public datasets.

At the very least, I hope that posts like this reduce the _conceptual
confusion_ about different types of reaction correctness.


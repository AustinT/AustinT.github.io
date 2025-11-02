---
title: "Justifying expected utility maximization from first principles (Von Neumann–Morgenstern)."
date: 2025-11-02
tags:
    - machine learning
    - statistics
    - opinion
has_math: false
---

I've recently found myself arguing for expected utility maximization as an
approach to practical decision making problems at work (mostly regarding
molecule selection). This post is my attempt to write out an argument for using
expected utility, targeted at non-mathematical (but still technical) readers.

<!-- TEASER_END -->

<div class="alert alert-warning">
<p>
<b>Disclaimer</b>:
No technical content in this post is original (I bet LLMs
can explain the same content just as well).
</p>
</div>

## Starter: the Von Neumann–Morgenstern utility theorem

I think the simplest path to expected utility is the Von Neumann–Morgenstern
(VNM) utility theorem. The VNM utility theorem essentially states that if you
have _preferences_ over uncertain outcomes, and these preferences obey a set of
axioms (aka rules), then there exists a utility function where maximizing
expected utility will always choose your most preferred option. My argument
will be to go through the axioms, and if you accept the axioms then expected
utility is the natural conclusion.

VNM operates specifically on preferences over "lotteries": essentially a
distribution over outcomes with known probabilities. Think of it like a
"mystery box" from a video game: you are given the odds of different boxes, but
must choose a box _without_ knowing exactly which outcome you will get.
Examples of a lunch lottery could be:

- A: 50% chance of hamburger, 50% pizza
- B: 25% dumplings, 25% bread, 50% sushi

We'll come back to framing other things as lotteries at the end of the post.

## The VNM axioms

The first axiom is **completeness**: for any lotteries A and B, you will either
prefer A, prefer B, or be indifferent between the options. I.e.: you can always
make a choice. This seems reasonable.

The second axiom of **transitivity**: if you prefer A to B, and B to C, then
you also prefer A to C. Hopefully this also seems reasonable.

The third axiom is **continuity**: if you prefer A > B > C, there is some
probability p (between 0 and 1) where the "nested" lottery "A with probability
p, C with probability (1-p)" is equally good as lottery B. This essentially
says that you are always willing to risk getting a worse option in exchange for
a chance at the best option at _some_ level of risk. For example, if you like
hamburger > pizza > sushi, for some level of risk p you would think "p chance
of hamburger, (1-p) chance of sushi)" is as good as 100% chance of pizza.
Hopefully this also seems reasonable.

The final axiom is **independence**: if you prefer A > B, then adding an
"irrelevant" nested lottery C should not change this preference, so pC + (1-p)A
\> pC + (1-p)B. For example, if you prefer hamburgers to pizza, then you should
prefer "95% chance getting hamburger, 5% salad" to "95% of getting pizza, 5%
salad" because the "5% salad" is the same on both sides. Hopefully this seems
reasonable.

## Possible objections to these axioms

I am the type of person who reads these axioms and happily accepts them all as
intuitively. For readers who don't have this reaction, or who have some
objections in mind, let me try to go through common critiques.

One possible critique comes from over-interpreting the goals or scope of these
axioms. These axioms are:

- **NOT** claims about how humans make decisions in the real world (humans can
  violate these, although it isn't a _terrible_ model either)
- **NOT** claiming that you must have a fixed set of preferences which does not
  change with time (a common but oversimplified model used in economics)
- **NOT** claiming that all _computer_ algorithms must follow these guidelines

All these axioms **are** is a description of preferences which (hopefully)
seems "reasonable". Here are responses to some individual sets of critiques
(click to open).


<details closed>
<summary><b>Objections to completeness</b></summary>

<ul>

<li><b>I don't always seem to have preferences (eg: choosing what to order at a
restaurant feels hard).</b> I think situations like this are an example of
<i>very weak</i> preferences (or pure indifference between different
options).</li>

<li><b>Some things seem undecidable (eg choosing between two bad options, like
"lose an arm or lose a leg").</b> I think these situations are overshadowed by
the unpleasantness of the choices, and the preference of "neither option".</li>

<li><b>Preferences change with time (eg sometimes I like pizza, sometimes I
like sushi).</b> The axioms don't say you as a person must hold a consistent
set of preferences over time, it just says when forced to make a decision at a
specific time there should be an underlying preference.</li>

<ul>
</details>

<details closed>
<summary><b>Objections to transitivity</b></summary>

This one is usually the least objectionable. The most common objection is
probably something like "in some situations I prefer A, in some situations I
prefer B", but this "objection" is just misinterpreting the axioms as assuming
preferences don't vary with time or context (see bullet point in previous box).

</details>

<details closed>
<summary><b>Objections to continuity</b></summary>

This axiom probably feels unintuitive because we aren't usually presented with
choices like this in real life. However, risking worse outcomes for a chance at
better outcomes is something people do all the time. Here are some
scenarios/responses:

<ul> <li><b>Extreme outcomes (eg "gain $100 vs lose your leg")</b>. You might
have the intuition that you would <i>never</i> take a gamble like that. I think
in practice this intuition just means that p would need to be very high. If p
is sufficiently close to 1 (eg 0.999999999999999999999999999999), the "bet"
starts to look like "free $100"). Another intuition pump: if we change $100 to
$1M, you might imagine taking the gamble with a slightly lower p).</li>

<li><b>An exact value for p isn't obvious (eg should p be 0.51 or 0.49).</b>
Fair, but if you accept some p value to be high enough that the gamble is worth
it (eg p=0.9999) and some level where p is too low (eg 0.00001), there must be
some p in the middle where it transitions. It might feel difficult to settle on
a precise number, but this is probably because in the general range of the
"right number" you would feel mostly indifferent (see "objections to
completeness" above).</li>

<li><b>Lexicographic preferences (eg "judge on price, then on quality, in
order, no trade-offs allowed").</b> This violates continuity because it does
not allow trade-offs. My objection to this is that being unwilling to make
trade-offs is, in most cases, very silly. Intuitions about "not having
trade-offs" are probably just intuitions that the trade-offs are very
steep.</li>

</ul>

</details>


<details closed>
<summary><b>Objections to independence</b></summary>

Historically this axiom has received a lot of criticism and debate in the
academic literature, but as far as I can tell most of this criticism is
directed at <i>utility maximization as a description of human decision
making</i>. Famous counter-examples like the Allais paradox show that humans
can violate independence in real-world gambling contexts. To resolve this,
remember that these axioms are <i>not</i> meant to be a description of real
human decision-making: instead they are descriptions of <i>rational</i>
decision making. I simply don't see how a decision maker violating independence
could be seen as an "intelligent" choice.

</details>

<br>
<br>

## Accepting the axioms leads to expected utility

I will not write out a proof here ([Wikipedia has a pretty good
one](https://en.wikipedia.org/wiki/Von_Neumann%E2%80%93Morgenstern_utility_theorem#Proof_sketch)),
but accepting these axioms directly implies the existence of a utility function
such that decisions for any lottery are made by maximizing expected utility.
Believing in these axioms _is_ believing in expected utility.

Of course, the VNM theorem is not stating that decision-makers operate by
_explicitly calculating_ expected utility (clearly they do not need to). It
only says that an expected-utility agent can _replicate_ the behaviour of
another agent by doing explicit expected utility calculations.

## Does this mean AI algorithms should calculate and maximize expected utility?

Sort of: it says it is a viable option. If decisions are made through a complex
process (eg human thought) but satisfy the VNM axioms, it means that direct
calculation is a viable alternative. However, there are many situations where
this is not possible:

- The odds of different outcomes are unknown (or hard/impossible to specify
  numerically)
- In a high-dimensional space it might be difficult to directly construct a
  utility function which represents a user's preferences (eg, think of learning
  art preferences directly in pixel space).
- In repeated rounds of decision making there is an exploration-exploitation
  trade-off which expected utility does not address

That being said, I am convinced that expected utility is a reasonable first
approach for many problems.

## Epilogue: how does this apply to molecules and other scientific problems?

In the context of such _scientific design_ problems (like molecule design in
drug discovery), scientists design high-dimensional objects (ie molecules) with
multiple (conflicting) objectives (eg potency, toxicity, solubility), each of
which is difficult to predict (and also difficult to measure experimentally). I
think each molecule can be thought of as a _lottery_, and its _properties_ are
the potentially uncertain outcomes.

The advantage of expected utility in this context is that it allows you to
decouple _uncertainty in outcomes_ from _preferences across multiple
objectives_, specify each one separately, then bring them together into a
principled decision-making algorithm. This is possible _if_ the chemists'
preferences satisfy the VNM axioms. Being humans, their past decisions might
not always follow it, but if the chemists agree that these axioms are
reasonable then it means constructing a utility function _is_ possible (at
least in theory).

Also, elucidating chemists preferences for hypothetical molecules with _known_
properties is much easier than for real molecules with unknown properties,
because their decisions will be a mix of preferences and property predictions.

I am personally hopeful that this approach (or an approach with this general
flavour) can be useful for getting AI to "work" for drug discovery, at least to
a degree that medicinal chemists are happy with!

---

## References

For this post I mostly referred to Wikipedia's page on this, which is very
good:
<https://en.wikipedia.org/wiki/Von_Neumann%E2%80%93Morgenstern_utility_theorem>.


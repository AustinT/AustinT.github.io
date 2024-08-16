---
title: "The Monty Hall Problem is Really About Policy Assumptions"
date: 2020-02-10
categories:
    - Statistics
    - frontpage
layout: post
mathjax: true
---

**TL;DR**: the Monty Hall problem doesn't have a well-defined solution.

The Monty Hall problem is a classic "probability paradox"[^1], where the answer
is counter-intuitive to most people's intuitions. To paraphrase [Wikipedia's
introduction to the
problem](https://en.wikipedia.org/wiki/Monty_Hall_problem)[^2]:

> Suppose you're on a game show, and you're given the choice of three doors:
Behind one door is a prize; behind the others, nothing. You pick a door, say No. 1,
and the host, who knows what's behind the doors, opens another door, say No. 3,
which has nothing. He then says to you, "Do you want to pick door No. 2?" Is it
to your advantage to switch your choice? 

This can be reframed as "what is the probability that the prize is behind door 2?"
The "_intuitive answer_" is 1/2 (meaning there is no advantage to switching),
since initially the prize could be behind any of the 3 doors, and you find out
that it isn't behind door #3, leaving just 2 doors left with equal probability
of having the prize.

In contrast, the "_correct answer_" is 2/3. This discrepancy is usually
explained away as the host _giving away_ information with their choice of which
door to open. Again, paraphrasing
[Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem#Simple_solutions):

> An intuitive explanation is that, if the contestant initially picks an empty door (2
of 3 doors), the contestant will win the prize by switching because the other
empty door can no longer be picked, whereas if the contestant initially picks the prize
(1 of 3 doors), the contestant will not win the prize by switching.

However, in this post I am arguing that **neither of these answers are
"correct"**, because the answer ultimately depends on your assumptions on what
actions the game show host would take in counterfactual situations. Since this
is not specified in most versions of the problem, the problem can't really be
said to have a "_correct answer_". After [introducing the math necessary to solve the problem](#bayesian-formulation-of-the-problem), I will work through some [example
assumptions](#examples) and their resulting implications, and conclude with the
surprising result that under the right assumptions, the answer to the problem
could be [**any** probability](#rigged-game-the-answer-could-be-anything).


## Bayesian Formulation of the Problem
Let:

- $$c$$ be the contestant's **c**oice of door
- $$o$$ be the door the host **o**pens
- $$a$$ be the **a**nswer (the door the prize is actually behind)

In a Bayesian decision framework, the way to handle this problem is to:

1. Use your knowledge of the situation to construct a probability distribution over the relevant variables ($$p(o,a,c)$$).
2. Use the values of the observed variables $$c$$ and $$o$$ to calculate the _posterior probability distribution_ over the answers: $$p(a\mid o,c)$$.
3. Use this probability distribution to make an informed choice. In this situation, reasonable choice would be to choose the most likely answer, $$a^* = \arg\max_a p(a\mid o,c)$$.

Therefore solving the problem is the same as finding the posterior distribution.
The posterior distribution can be found using Bayes theorem:

$$p(a\mid o,c) = \frac{p(o,a,c)}{p(o,c)} = \frac{p(o,a,c)}{\sum_{a'} p(o,a',c)}$$

This is far as we can go without making any assumptions. The most basic
assumptions (which aren't that interesting) is that the game is fair ($$a$$ is
chosen randomly in advance) and real (the player doesn't know anything about
$$a$$, so their choice is effectively random).
This means that the only interesting behaviour is that of the host,
who can choose which door to open, knowing both where the prize is and the player's choice.
Mathematically, this means that the distribution $$p(o,a,c)$$ can be _factored_ as:

$$p(o,a,c) = p(a)p(c)p(o\mid a,c)$$

Substituting this into the posterior equation above, and nothing that $$p(c)$$ is
a constant and cancels, we find:

$$p(a\mid o,c) = \frac{p(o,a,c)}{\sum_{a'} p(o,a',c)} = \frac{p(o\mid a,c)p(a)p(c)}{\sum_{a'}p(o\mid a',c)p(a')p(c)} = \frac{p(o\mid a,c)p(a)}{\sum_{a'}p(o\mid a',c)p(a')}$$

Assuming further that all answers are equally probable, this further simplifies to:

$$p(a\mid o,c) = \frac{p(o\mid a,c)}{\sum_{a'}p(o\mid a',c)}$$

This means that for this particular problem,
the posterior can be computed with only 3 values:
$$p(o=3\mid a_i, c=1)$$, $$i\in\{1,2,3\}$$.

## Examples

### Standard assumptions: the argument for 2/3

When most people hear this problem, beyond the assumptions outlined in
[the previous section](#bayesian-formulation-of-the-problem), they usually assume the following things:

1. the host will not open the door with the prize behind it
2. the host will not open the player's door
3. the host will always open a door
4. if the host can open multiple doors, they will choose one at random

Assumptions 1-2 make sense, because otherwise the game show might not be any
fun to watch. Assumption 3 isn't necessary but is usually assumed because when
people imagine this game show they usually imagine that this switching gimmick
is just part of the show. Assumption 4 makes sense, since there is no reason _a
priori_ to assume that the host will be biased towards any particular door.

With this, we can calculate the 3 values of $$p(o\mid a,c)$$:

1. $$p(o=3\mid a=1,c=1)=1/2$$: the host could open doors 2 or 3 here, and would
   therefore pick at random. This would have them pick door 3 50% of the time.
2. $$p(o=3\mid a=2,c=1)=1$$: here the host cannot choose door 1 (since the player
   chose it) or door #2 (since it has the prize), so opening door #3 is the only
   option
3. $$p(o=3\mid a=3,c=1)=0$$: if door #3 had the prize, the host wouldn't have opened
   it, so this event isn't possible.

So, $$p(a=2\mid o=3,c=1) = \frac{1}{1/2+1} = 2/3$$,
suggesting that the best choice is to pick door 2 (switch doors).
This is the classic "correct answer" of 2/3.

### Biased random choice of host

Suppose that assumption 4 above isn't true:
when the host has multiple doors that they could choose,
they don't make a truly random decision[^3].
One example of this is if the host tends to pick higher numbers over lower numbers:
that is, given a choice of opening doors 2 or 3, they will pick door 3 with probability $$z$$,
which might not be $$1/2$$.

This scenario is similar to the standard one, except $$p(o=3\mid a=1,c=1)=z$$, so
$$p(a=2\mid o=3,c=1)=\frac{1}{1+z}$$, which can vary between 1/2 and 1 for different
values of $$z$$. Already, this formulation (which isn't completely unrealistic)
gives a huge range of possible answers, all contingent on your belief about how
the host picks random numbers.

### Inattentive host

Suppose the host didn't see what door the player chose. The host's decision
then can't depend on $$c$$ (breaking assumption 2). Instead, the host will
randomly open one of the doors that doesn't have the prize, regardless of
whether the player chose this door. This means $$p(o=3\mid a=i,c=1)=1/2$$ for
$$i=1,2$$ ($$i=3$$ remains unchanged since the host won't open the door with
the answer behind it). Therefore, $$p(a=2|o=3,c=1)=1/2$$. This scenario is
certainly plausible in a real game show (although fairly unlikely).

### No door as an option

If the host can choose _not_ to open a door, this opens up a wide range of possibilities:

#### Dramatic host 1

To make the show more entertaining to watch, the host wants to bait the player
into switching doors, not getting the prize, and then watch them agonize over
their decision to switch. One way to do this would be to only open a door if
the player's initial guess was correct.

This means $$p(o=3\mid a=1,c=1)=1/2$$, and the other 2 probabilities are 0, so the
posterior probability $$p(a=2\mid o=3,c=1)=0$$.

#### Dramatic host 2

Dramatic host 1 is too predictable (since being offered to switch doors means
you should never switch). Dramatic host 2 becomes slightly less predictable by
choosing with probability $$q$$ to open a wrong door if the player initially
chose correctly. This means that $$p(o=3\mid a=1,c=1)=1/2$$ (like last time), but
$$p(o=3\mid a=2,c=1)=q$$, making the posterior probability
$$p(a=2\mid o=3,c=1)=\frac{q}{1/2+q}$$, which can range from 0 to 2/3.

#### Merciful host

Instead, a host could open a door only if the player's initial choice was
wrong, yielding a posterior probability $$p(a=2\mid o=3,c=1)=1$$. In this case, you
would always want to switch doors if offered.

#### Only door 3 can be opened

Imagine that the host will act normally (i.e. standard assumptions), but if the
final decision is to open doors 1 or 2 they will simply not open a door at all
(they are only willing to open door 3)[^4]. This means that $$p(o=3\mid a=1,c=1)=1$$,
so the posterior $$p(a=2\mid o=3,c=1)=1/2$$.

## Rigged game: the answer could be anything

Suppose that our initial model of the causal process is wrong, and the game is
unfair. Specifically, the player chooses a door, and then the correct door is
chosen afterwards with this information[^5]. 
Specifically, suppose that the producers select the player's door as correct
with probability $$q$$, and one of the other 2 doors with probability $$1-q$$.
Note that if $$q=1/3$$, this corresponds to the standard assumptions of a fair game.

To calculate the posterior in this scenario, we need $$p(a\mid c)$$ and $$p(o\mid a,c)$$,
which are the following:

- $$p(a=1\mid c=1) = q$$ (by assumption above)
- $$p(a=2\mid c=1) = p(a=3\mid c=1) = (1-q)/2$$ (since the probabilities must add to 1)
- Since the hosts actions don't change, $$p(o\mid a,c)$$ is the same as before
  ($$p(o=3\mid a=1,c=1)=1/2$$, $$p(o=3\mid a=2,c=1)=1$$, $$p(o=3\mid a=3,c=1)=0$$)

Reapplying Bayes rule, we get:

$$p(a\mid o,c) = \frac{p(o\mid a,c)p(a\mid c)}{\sum_{a'}p(o\mid a',c)p(a'\mid c)}$$

$$p(a=2\mid o=3,c=1) = \frac{1\times(1-q)/2}{q/2 + 1\times(1-q)/2 + 0\times(1-q)/2} = 1-q$$

Since $$q$$ can take on any value between 0 and 1, the posterior value can be any
value between 0 and 1, meaning that the right decision could be **absolutely
anything**. Of course, this is far from what most people assume when they
encounter the Monty Hall problem, but if you were actually on such a game show
in real life and offered this deal, would it not be prudent to at least
consider this possibility?

## Conclusion

In this post, I've shown how [Bayes rule](#bayesian-formulation-of-the-problem)
can be used to solve the Monty Hall problem, which under [standard
assumptions](#standard-assumptions-the-argument-for-23) gives the "correct
answer" of 2/3. However, under different assumptions, the posterior probability
of the prize being behind door 2 can take on many different values, which
between a [biased host](#biased-random-choice-of-host) and a host that wants to
[make you lose](#dramatic-host-2) spans the whole range of probabilities
between 0 and 1. In fact, just assuming that the game isn't fair yields a model
where it could be better to switch with probabilities ranging from 0 to
1 inclusive!.

Overall, it's very misleading to suggest that this is just a simple problem
that tests if you can do some algebra; the entire solution is **completely
determined** by one's beliefs about the host's counterfactual actions, so it's
frankly surprising that this aspect of the problem isn't more widely discussed.
As always, while an explicit Bayesian formulation isn't required to arrive at
the desired answer, the Bayesian framework does aid greatly in making your
assumptions explicit.

[^1]: Specifically it would be a [veridical paradox](https://en.wikipedia.org/wiki/Paradox#Quine's_classification), because the result appears absurd but is nonetheless true.

[^2]: the original version used cars and goats, which I changed to just a prize/nothing for clarity.

[^3]: since people are generally quite bad at choosing truly random numbers

[^4]: maybe they are superstitious and like the number 3?

[^5]: The producers of the game show might do this to increase the amount of dramatic tension on the show. Who says that "reality" TV needs to be real?

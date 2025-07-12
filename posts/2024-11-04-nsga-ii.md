---
title: "Overview of the NSGA-II algorithm for multi-objective optimization"
date: 2024-11-04
tags:
    - research papers
    - frontpage
has_math: true
---

Nondominated sorting genetic algorithm version 2,
more commonly called NSGA-II, is a well-established genetic algorithm
(aka evolutionary algorithm)
for multi-objective optimization (MOO).
In this post I try to extract the key insights/lessons from this paper.

<!-- TEASER_END -->

Disclaimer: this blog post is almost certainly _not_ the best piece of content
on the internet about NSGA-II.
I wrote it mainly to help myself understand the algorithm.
If you want to learn about the algorithm you may wish to read any one of the hundreds
of articles written about it since its initial publication 20+ years ago.

## Preamble: why should I care about NSGA-II?

Genetic algorithms (GAs) are very clearly not "cool" anymore,
and their shortcomings are well-known.
Despite this, NSGA-II seems to have been very widely-used.
As I am writing this post,
the paper proposing NSGA-II[^Deb2002] has been cited
over 50000 times (according to Google scholar).
In fact, there are entire papers
(like [this one](https://link.springer.com/10.1007/s10462-023-10526-z))
which summarize the usage of this algorithm.
Clearly, something about NSGA-II _works_ for real-world MOO,
or at least works well enough to be used more than most other algorithms.

## Key to NSGA-II: a thoughtful partial ordering

Like other GAs, NSGA-II keeps a set of candidate solutions.
In each phase of the algorithm,
this set is first _grown_ by 
randomly "mutating" and re-combining existing candidates,
then _pruned_ to keep only the most promising candidates.
NSGA-II's contribution targets the second "pruning" step:
it proposes a way to select a subset of candidates which:

- Prioritizes non-dominated (aka Pareto-optimal) solutions
- Respects constraints (if constraints exist)
- Promotes diversity among candidates

It accomplishes this by defining a _partial ordering_
$\prec_{n}$ over the candidate set (by our convention, lower is better).
It then uses $\prec_{n}$
to perform a [topological sort](https://en.wikipedia.org/wiki/Topological_sorting)
of the candidate set
(ie an ordering $[x_1, \ldots, x_N]$ such that if $x_i\prec x_j$ then $i < j$).
The first $P$ candidates from this set are chosen to be the next candidate set-
that's it.
All the logic to prioritize non-domination/diversity/constraint satisfaction goes
into the definition of $\prec_{n}$.

The original paper does not write out the entire algorithm for $\prec_{n}$,
so for clarity I will try to do so here.
The algorithm uses the following operators:

- _objective domination_ partial ordering $\prec_{o}$
(ie $x_i\prec_{o} x_j$ if $x_i$  differs from $x_j$ in at least one objective and is better than or equal to $x_j$ in _every_ objective).
- Scalar _constraint violation function_ $g(x)$. $g(x)=0$ if $x$ satisfies the problem constraints, otherwise a positive value (higher values are worse).[^1]
- _Crowding distance_ $c(x)$ (how close $x$ is from other candidate solutions). Lower is better. Can be implemented in multiple ways (and this seems to be one of the most frequently varied parts of the algorithm)

As far as I can tell,
the actual procedure to evaluate the statement $x_i\prec_{n} x_j$ (which can take the values **true**, **false**[^2], or **not-comparable (NC)**) is:

1. **Prioritize constraint satisfaction**: if $g(x_i) < g(x_j)$ return **true**. If $g(x_j) < g(x_i)$: return **false**. Otherwise, go to next step.
2. **Check objectives**: if $x_i \prec_{o} x_j$: return **true**. If $x_j \prec_o x_i$: return **false**. Otherwise, go to next step.
3. **Break ties by crowding**: if $c(x_i) < c(x_j)$: return **true**. If $c(x_j) < c(x_i)$: return **false**. Otherwise, go to next step.
4. Return **NC**

Owing to the first condition,
the partial ordering $\prec_n$ will partition the candidates into two sets: those satisfying constraints (ie tied for $g(x)=0$), and those that do not.
Candidates _satisfying_ the constraints are ordered first by non-domination ($\prec_o$), then by crowding for tie-breaking.
Candidates _not_ satisfying the constraints will first be ordered by constraint violation, and the same procedure as other points
is used in case of a tie.

## Why does NSGA-II work well?

Put together, the partial ordering $\prec_n$ ensures a number of desirable properties:

- Candidates satisfying constraints are prioritized as much as possible
- The current Pareto front is always preserved, if possible (this property is called _elitism_ in the paper, probably because "elite" samples are always favored)
- If the entire Pareto front cannot be preserved, it will try to eliminate points from "crowded" regions

One way to think of NSGA-II is that it separates the candidates into a sequence of _non-dominated fronts_:
a first front wherein no point dominates any other, a second front whose points are only dominated by those in the first front,
a third front whose points are only dominated by those in the first two fronts, and so forth.
The heuristic of taking points from the first front, then from the second front, etc is simple and intuitive.

Importantly, NGSA-II _does not_ require the user to input hyperparameters about how to trade-off diversity vs optimality,
which are probably difficult to tune.
The authors furthermore include a fast algorithm for non-dominated sorting
which scales with $O(MN^2)$ for $N$ candidates and $M$ objectives,
allowing the algorithm to be run with reasonably large populations.

## Problems with NSGA-II

Reading a little bit into the literature (and asking ChatGPT),
it seems that NSGA-II struggles with problems
with many objectives (large $M$)
and in high dimensions.
Both struggles are understandable.
With many objectives the potential size of a non-dominated set could get very large,
potentially requiring a massive population.
Since NSGA-II's selection scales quadratically with population size, this can quickly become
infeasible.
Furthermore, in high dimensions it is likely difficult to design a good crowding function $c$.

## Conclusions

Ultimately, my takeaways from this paper are:

- How to trade-off between different objectives is a difficult challenge in MOO. NSGA-II shows that we can just sort candidates into sequential non-dominated fronts and prefer points from the outermost front as much as possible.
- Using diversity only as a tie-breaker can make sense.
- Using a partial ordering instead of a full ordering lets one avoid setting trade-off hyperparameters

I would be curious if anybody has applied NSGA-II to molecules.
If I have time I might try to put it into my [`mol_ga`](https://pypi.org/project/mol-ga/) package.

[^Deb2002]: <https://ieeexplore.ieee.org/abstract/document/996017>

[^1]: Unconstrained problems are represented as $g(x)=0 \forall x$

[^2]: implying $x_j\prec_{n} x_i$

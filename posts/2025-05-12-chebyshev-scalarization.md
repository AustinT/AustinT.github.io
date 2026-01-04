---
title: "Chebyshev Scalarization Explained"
date: 2025-05-12
tags:
    - machine learning
    - bayesian optimization
    - _all-time-best
has_math: true
---

I've been reading about multi-objective optimization recently.[^surprise]
Many papers state limitations of "linear scalarization" approaches,
mainly that it might not be able to represent all Pareto-optimal solutions
(if this sentence does not make sense to you, see [background](#background-to-multi-objective-optimization)).
Chebyshev scalarization is sometimes mentioned as an alternative which _can_ represent all solutions.
However, these papers mention it in passing without a proper explanation,
and I did not find a good explanation of it online.[^online]

After doing a bit of my own research,[^gemini] I found that Chebyshev scalarization is actually not too complicated, so I thought _I_ would explain it online.
In this post, I:

- Give definitions for Chebyshev scalarization (for both maximization and minimization)
- Give a simple proof that it can represent all Pareto-optimal solutions
- Explain its relationship to linear scalarization via $\ell_p$ norms.
- Give a geometric interpretation via an interactive visualization

<!-- TEASER_END -->

[^surprise]: Since real-world drug design problems are always multi-objective (e.g. potency, toxicity, cost), this shouldn't be very surprising!

[^online]: More information about my sources is in the [references section](#some-references).

[^gemini]: Aided by Gemini 2.5, which was surprisingly helpful!

<div class="alert alert-info">
  <h4>Notation and Acronyms</h4>
  <ul>
    <li><strong>MOO</strong>: multi-objective optimization</li>
    <li>Bold denotes vectors (eg $\mathbf{f}$), $f_i$ is element of a vector</li>
  </ul>
</div>

## Background to multi-objective optimization

_Feel free to skip to [the next section](#chebyshev-scalarization) if you are familiar with this field, my notation and definitions are fairly standard_.

### Multi-objective optimization (MOO)

The goal of _multi_-objective optimization is to optimize a k-dimensional vector-valued function
$\mathbf{f}: \mathcal{X} \mapsto \mathbb{R}^k$ ($\mathcal{X}$ is an arbitrary input space).
_Optimize_ can mean maximize or minimize. In this post I will generally assume _maximization_.
This means we want to find a _single_ point $x\in\mathcal{X}$ where $\mathbf{f}(x)$ is
as large as possible in each dimension.[^max]

[^max]: Some papers write $\max_{x\in\mathcal{X}} \mathbf{f}(x)$. This captures the _spirit_ of the problem, but is not a well-defined mathematical expression. I always cringe when I see this 😬

### Pareto optimality and non-domination

Although MOO is a problem in $\mathcal{X}$ space,
the remainder of this post will only discriminate between points
$x$ via their values of $\mathbf{f}(x)$.
Therefore we will drop the dependence on $x$ and simply write $\mathbf{f}$
for the remainder of the post (and always assume there is a point $x$ attached to $\mathbf{f}$).
This should not cause any ambiguity.

If a point $\mathbf{f}$ is at least as large as a point $\mathbf{f}'$ in _every_ dimension
and exceeds $\mathbf{f}'$ in _at least one_ dimension,
we say that $\mathbf{f}$ _dominates_ $\mathbf{f}'$
and write[^succ] $\mathbf{f}\succ \mathbf{f}'$.

[^succ]: We use $\succ$ instead of $>$ because "domination" is only a partial ordering.

Unlike in single-objective optimization,
there may not be a single dominant point $\mathbf{f}^\ast$.
For example, in the set $\\{[0, 1], [1, 0]\\}$, neither point dominates the other: they are both better in one dimension and worse in the other.
Therefore, MOO generally seeks points
$\mathbf{f}^*$ which are _not dominated_ by any other vector $\mathbf{f}$.
Such vectors are called _Pareto optimal_,
and the collection of all such vectors is called the _Pareto set_.

For a more precise definition, see this footnote.[^paretodefn]

[^paretodefn]: Is the Pareto set a subset of $\mathcal{X}$ or $\mathbb{R}^k$? It can be both depending on the context. For this post I will define the Pareto set to be a subset of $\mathbb{R}^k$, specifically the set of all non-dominated vectors in the image of $\mathcal{X}$ under $\mathbf{f}$. $$\\{\mathbf{f}(x)| x\in\mathcal{X} \text{ and } \not\exists y\in\mathcal{X} : \mathbf{f}(y)\succ \mathbf{f}(x)\\}$$ However, in the broader context of MOO I think the Pareto set should _really_ be the set of all inputs $x$ which achieve these Pareto optimal values. I've mainly chosen the first definition for simplicity in this post.

### Scalarization: turning multi-objective optimization into single-objective optimization

Optimization algorithms which are _truly_ multi-objective will look very different from single-objective optimization algorithms because they need to find a Pareto set and explore different trade-offs between the k objectives.
This is a shame, since single-objective optimization is well-studied and many useful algorithms have been developed.
_Scalarization_ is essentially an attempt to turn a MOO problem into a _set_ of single-objective problems via a set of _scalarization functions_
$$\\{s_\theta: \mathbb{R}^k\mapsto \mathbb{R}\\}_{\theta\in\Theta}\ .$$

Each scalarization function assigns a single (scalar) score to the vector-valued output of $\mathbf{f}$.
The most common type of scalarization is _linear scalarization_, aka "weighted sum":
$$s_{\mathbf{w}}(\mathbf{f}) = \sum_i w_i f_i$$
where $\mathbf{w}=[w_1,\ldots,w_k]$ is a vector of positive weights.

One would hope to find Pareto optimal points by optimizing $s_\theta(\mathbf{f}(x))$ for various values of $\theta$.
Clearly this will not actually produce Pareto optimal points for _any_ functions $s_\theta$.
However:

- If the scalarization functions are are _strictly monotonically increasing_ in all of their inputs, then the _maximizer(s)_ of the scalarization function must all be Pareto optimal.
- If the scalarization functions are _non-decreasing_ (ie non-strictly monotonically increasing), then the set of maximizers will _contain_ Pareto optimal points, but may also include sub-optimal points.

Hopefully this makes intuitive sense, otherwise see [these theorems](#a-scalarization-and-monotonicity).

## Chebyshev scalarization

### Definition

Chebyshev scalarization[^spelling] functions take two parameters:

[^spelling]: Sometimes also spelled Tschebyschev or Tchebycheff, but I will just use Chebyshev.

1. A vector of positive weights $\mathbf{w}$ (like linear scalarization)
2. A _reference point_ $\mathbf{z}\in\mathbb{R}^k$, interpreted as the _ideal value_ for $\mathbf{f}$.

Scalarization was introduced previously as a set of functions $s_\theta$ to be _maximized_.
In this form, the function is:

$$s_{\mathbf{w}, \mathbf{z}}(\mathbf{f}) = s_{\mathrm{Cheby(max)},\mathbf{w}, \mathbf{z}}(\mathbf{f}) = - \max_i \left[ w_i|f_i - z_i|\right]\ .$$

Note that by maximization, I mean that $s$ is to be maximized, not $\mathbf{f}$.
The form is _the same_ regardless of whether $\mathbf{f}$ is to be maximized or minimized- that information
is encoded by the _reference point_ $\mathbf{z}$.

Importantly, notice the _negative sign_: it means that this function is always _negative_.
This is because Chebyshev scalarization is normally defined as a scalar to be _minimized_.
This alternative (and more natural) definition is:

$$ s_{\mathrm{Cheby(min)},\mathbf{w}, \mathbf{z}}(\mathbf{f}) = \max_i \left[ w_i|f_i - z_i|\right]\ .$$

$s_{\mathrm{Cheby(min)},\mathbf{w}, \mathbf{z}}(\mathbf{f})$ and
$s_{\mathrm{Cheby(max)},\mathbf{w}, \mathbf{z}}(\mathbf{f})$
differ only by a negative sign.
I will mainly use the (max) variant in this post for consistency.

### Interpretation

Chebyshev scalarization is essentially a _penalty_ equal to the largest deviation
between $\mathbf{f}$ and the reference point $\mathbf{z}$ across any dimension,
with all deviations re-scaled by the weight vector $\mathbf{w}$.
It is optimized when this penalty is _smallest_ (hence the negative sign when it is maximized).

Dimension-wise maximum is essentially the definition of the $\ell_\infty$ norm,
also called the Chebyshev norm. This is actually where Chebyshev scalarization gets its name.[^name]
In this form, it is:

$$s_{\mathbf{w}, \mathbf{z}}(\mathbf{f}) = -\left\| \mathbf{w}\odot \left(\mathbf{f} - \mathbf{z} \right) \right\|_\infty \ .$$

[^name]: I think "$\ell_\infty$-scalarization" would be a better name than Chebyshev scalarization, but it's hard to change an established name 🫠

Therefore, think of Chebyshev scalarization as "distance to reference point in a different norm."

### Pareto coverage property

This is the most important property of Chebyshev scalarization.

_**IF** $\mathbf{z} > \mathbf{f}$ in each dimension for all achievable points $\mathbf{f}$_, then:

1. All Pareto-optimal points maximize 
  $s_{\mathbf{w}, \mathbf{z}}(\cdot)$ for some positive weight vector $\mathbf{w}$.
2. For any positive weight vector $\mathbf{w}$, maximizing 
  $s_{\mathbf{w}, \mathbf{z}}(\cdot)$ will produce at least one Pareto-optimal point.

This means:

1. Picking a weight vector $\mathbf{w}$ and maximizing $s_{\mathbf{w}, \mathbf{z}}(\cdot)$ will produce a Pareto optimal point (although it may also produce additional maximums for sub-optimal points). Useful, but this is not surprising since, if $\mathbf{z} > \mathbf{f}$ element-wise, then the function is non-decreasing and [proposition A.2](#a-scalarization-and-monotonicity) applies.
2. **ALL** Pareto-optimal points can be produced by picking a suitable vector $\mathbf{w}$.
3. These properties **do not** depend on a specific value of the reference point $\mathbf{z}$ (as long as it is an unachievable high value).

Property 2 is what distinguishes Chebyshev scalarization from linear scalarization
(which can only find points on the convex hull of the Pareto frontier).
[At the end of this post](#b-chebyshev-coverage-of-pareto-front)
I give a simple proof by construction of point 2,
which essentially amounts to setting $w_i = 1/\left(z_i-f_i\right)$.

_(NOTE: for minimization of $\mathbf{f}$, simply replace the condition $\mathbf{z} > \mathbf{f}$ with $\mathbf{z} < \mathbf{f}$) and the same result will hold._

### Note about the weights

Because one can factor a multiplicative constant out of the weights, it suffices to consider only weights which sum up to 1:
$$\mathbf{w}: \sum_i w_i = 1\ .$$
This is true for Chebyshev _and_ linear scalarization.

## Comparison with linear scalarization

[Earlier](#interpretation) I stated that Chebyshev scalarization is essentially minimizing the $\ell_\infty$
norm between $\mathbf{f}$ and $\mathbf{z}$.
Linear scalarization actually has a close connection to the $\ell_1$ distance between
$\mathbf{f}$ and $\mathbf{z}$.

Assume that we have a reference $\mathbf{z}$ where $\mathbf{z} > \mathbf{f}$ element-wise
(just as [done previously](#pareto-coverage-property) to get Pareto coverage for Chebyshev scalarization).
Then, we write

$$-\left\| \mathbf{w}\odot \left(\mathbf{f} - \mathbf{z} \right) \right\|_1  = -\sum_i w_i \left|f_i - z_i \right| =\sum_i w_i f_i - \sum_i w_i z_i$$

(Step-by-step explanations in footnote[^stepbystep])
The first time is linear scalarization. The second term is _constant_ with respect to the input vector $\mathbf{f}$,
and therefore will not change which inputs _maximize_ the scalarization.
This allows the reference point to be _excluded_ from the scalarization without consequence,
but also allows us to _include_ a reference point in linear scalarization without consequence.

[^stepbystep]: First use definition of $\ell_1$ norm, then note that $f_i-z_i$ always negative by the assumption that $\mathbf{z} > \mathbf{f}$ in every dimension, then cancel with minus sign at front and distribute the product.

_Summary: Chebyshev and linear scalarization can both by interpreted as $\ell_p$ distances between objectives
and an unattainable reference point.
Linear scalarization uses $p=1$, and you can manipulate the expression to put the reference point in an additive constant.
Chebyshev scalarization uses $p=\infty$ and does not allow you to separate
out the reference point._

## Augmented Chebyshev

Because Chebyshev scalarization is not _strictly_ monotonic,
there may be some maximizers which are not Pareto optimal.
This can be fixed by _augmenting_ it with a linear scalarization term,
weighted by a factor $\rho > 0$:
$$s_{\mathrm{Cheby(aug)},\mathbf w, \mathbf z, \rho} = - \max_i \left[ w_i|f_i - z_i|\right] + \rho\sum_i w_i f_i \ .$$

This _augmented Chebyshev_ function is _strictly_ monotonic, and therefore all maximizers will be Pareto optimal.
Unfortunately, this function _does not_ guarantee that all Pareto optimal points can be found,
although a sufficiently small value of $\rho$ makes this likely in practice.

## Geometric interpretation

To build understanding, I made an interactive visualization comparing linear, Chebyshev, and augmented Chebyshev scalarization.
**Disclaimer**: this was vibe-coded with Cursor and definitely isn't perfect;
I just had no experience using plotly before.
The visualization will probably work much better on desktop compared to mobile (apologies 🙏).
If you want to modify / improve the visualization,
check out the source code 
[here](https://github.com/AustinT/2025-chebyshev-scalarization).

The visualization shows 3 types of Pareto fronts in $\mathbf{f}$ space:
convex (default), concave, and mixed.
The feasible region is marked in blue.
You can switch between Pareto front types using the drop-down menu.

Because this is a 2D problem, we can set $w_2=1-w_1$ and just look at the scalarizations as a function of $w_1$.
The bottom slider controls $w_1$ for all scalarizations simultaneously.
All scalarizations use the reference point $\mathbf{z} = [1.1, 1.1]$ (which dominates all points in the feasible region for all examples).

The feasible point which maximizes the scalarization is marked with a black dot
(if several points are tied then there may be multiple black dots).
The level sets of the scalarizations are shown with contour lines (hopefully making it clear where the maximum comes from).

I suggest you take some time to play around with the visualization now
(otherwise I provide a summary below).

<!-- Include visualization div directly -->
<div class="visualization-container">
    <div class="visualization-container" >
      <object type="text/html" data="/blog-images/2025-chebyshev/multi_objective_scalarization.html" width="100%" height="700px"></object>
  </div>
</div>

### My analysis of visualization

First, note the shapes of the level sets. For "Linear" they are parallel lines.
For Chebyshev they are square-like (which should not be surprising since the $\ell_\infty$ unit ball is a square).
For augmented Chebyshev they are _almost_ square, except the angle is a bit larger than 90°.

Now, let's compare the behavior as $w_1$ ranges from 0 to 1:

- For the "convex" Pareto front, all 3 functions sweep across the entire front. The maximum point is always tangent[^tangent] to a level set.
- For the "concave" Pareto front:
    - Linear scalarization completely fails. For $w_1<0.5$ the maximum is near the top left, and for $w_1>0.5$ it suddenly shifts to the bottom right.[^half] This is a well-understood limitation of linear scalarization.
    - Chebyshev scalarization nicely sweeps across the entire front. However, note that for very small or very large values of $w_1$ there is a tie and a small number of dominated points also maximize the objective.
    - Augmented Chebyshev also covers the entire front, but does not include duplicate points at the end (NOTE: at $w_1=0.5$ 2 points appear, but this is just an artifact of the maximization being done on a finite grid, the true maximum should be between those two points).
- For the "mixed" Pareto front:
    - Linear scalarization finds the two convex sections, but completely skips the concave part (looking at the level sets should make it clear why this is).
    - Chebyshev scalarization sweeps across the entire front, but for several values of $w_1$ around 0.25 and 0.75 a few dominated points are included (see small vertical or horizontal lines of black dots).
    - Augmented Chebyshev scalarization sweeps across _most_ of the front, but if you look carefully, some parts of the concave region are actually skipped (look for a big jump around $w_1\approx 0.45$ which does not appear for Chebyshev). It should be clear that this is caused by the level sets not being "pointy" enough to reach into all parts of the concavity. If $\rho$ were decreased then this problem would be reduced.


[^tangent]: I'm counting points on a corner as "tangent" too.

[^half]: Note that nothing is _intrinsically_ special about the value 0.5, the switch only happens here because the feasible region is symmetric between $f_1$ and $f_2$. For other concave objectives the critical value might be different.

## Conclusion

This post explained Chebyshev scalarization, which is essentially a weighted $\ell_\infty$ distance
to a reference point.
Its main advantage is its ability to cover _every_ point on a Pareto front,
while its main disadvantage is that it can be maximized by some dominated points.
Another potential disadvantage is that it requires specifying a reference point which is guaranteed
to dominate all other points.
Its Pareto coverage property does not depend on the exact _value_ of this reference point,
but it _must_ dominate all points, and it does affect which point(s) are optimal for
a given value of $\mathbf{w}$.

Augmented Chebyshev has properties in between that of Chebyshev and linear scalarization:
it may not cover _every_ point on a Pareto front, but will likely cover _most_ points,
especially when $\rho$ is small.
However, dominated points will _not_ maximize augmented Chebyshev.

Perhaps another middle ground is the
$\ell_p$ distance with large $p$.
The level sets would be "pointier", but the function would still be strictly monotonic in all its inputs.


Ultimately, I think Chebyshev scalarization is a good idea and people should try to use it!

---

## Theorems and proofs

### A: Scalarization and monotonicity

The following propositions show that strictly monotonic functions are only maximized by Pareto-optimal points,
and that non-strictly monotonic functions are _at least_ maximized by Pareto-optimal points
(although other maximizers may not be Pareto optimal).

**Proposition A.1**:
if $s: \mathbb{R}^k\mapsto\mathbb{R}$ is strictly monotonically increasing,
then all maximizers
$$\mathbf f^\ast\in\arg\max_{\mathbf{f} \in \mathbf{f}(\mathcal{X})} s(\mathbf{f})$$
must be Pareto optimal.

**Proof**:
Assume a $\mathbf f^\ast$ is _not_ Pareto optimal,
then there is another point $\mathbf f ' \succ\mathbf f^\ast$.
By monotonicity, $s(\mathbf f') > s(\mathbf f)$,
because $f'_i \geq f_i$ in all dimensions
(showing $s(\mathbf f') \geq s(\mathbf f)$),
and $f'_i > f_i$ in at least 1 dimension,
thereby getting strict inequality.
Therefore, $s(\mathbf{f}^\ast)$ must not actually be a maximizer: a contradiction.

**Proposition A.2**:
if $s: \mathbb{R}^k\mapsto\mathbb{R}$ is non-strictly monotonically increasing,
then the set
$$M=\arg\max_{\mathbf{f} \in \mathbf{f}(\mathcal{X})} s(\mathbf{f})$$
must contain at least one non-dominated point.

**Proof**:
Similar to above. Assume it _does not_ contain a non-dominated point,
and let $\mathbf{f}^\ast\not\in M$ be a point which dominates at least one
point in $M$ (call it $\mathbf{f}$).
By monotonicity, we must have that $s(\mathbf{f}^\ast) \geq s(\mathbf{f})$,
and therefore it should be that $\mathbf{f}^\ast\in M$: a contradiction.

### B: Chebyshev coverage of Pareto front

Here I provide a simple proof by construction for Pareto front coverage.
Note that this is not my original proof.

**Proposition B.1**:
If $\mathbf{z} > \mathbf{f}$ in each dimension,
then 
all Pareto-optimal points maximize 
$s_{\mathbf{w}, \mathbf{z}}(\cdot)$ for some positive weight vector $\mathbf{w}$.

**Proof**:
Let $\mathbf f^\ast$ be a Pareto optimal point, and construct $\mathbf w$ by
$$w_i = \frac{1}{z_i - f^\ast_i}\ .$$
Note that $w_i>0$ for all $i$ because $z_i>f_i^\ast$ by assumption.
Then
$$s_{\mathbf{w}, \mathbf{z}}(\mathbf f ^\ast) = - \max_i \left[ w_i|f_i^\ast - z_i|\right]=-\max_i \left[ \frac{z_i-f_i^\ast}{z_i-f_i^\ast} \right] = -1\ .$$

Now, assume that for some other $\mathbf{f}$, 
$s_{\mathbf{w}, \mathbf{z}}(\mathbf f) > -1$.
For this to happen, for _all_ $0\leq i \leq k$
$$\frac{z_i-f_i}{z_i - f_i^\ast} < 1 \Rightarrow f_i^\ast < f_i\ .$$
This would imply $\mathbf f \succ \mathbf f^\ast$, contradicting the assumption that
$\mathbf f^\ast$ is Pareto optimal!

---

## Some references

Here are some references which I relied on to write this post:

- Wikipedia has a page ([link](https://en.wikipedia.org/wiki/Chebyshev_function)),
  but it describes 2 different kinds of function, and only describes the function for minimizing $\mathbf{f}$.
- An [old paper by Steuer & Choo (1983)](https://link.springer.com/article/10.1007/BF02591870)
  describes random Chebyshev scalarization and basically covers the same material as this post,
  but with denser notation and more theorems (such that the key points are harder to ascertain).
- [This NeurIPS paper by Lin et al](https://proceedings.neurips.cc/paper_files/paper/2022/hash/7a583691ccfcf8945ab714b677ccbf0b-Abstract-Conference.html)
  re-states some of this content more clearly,
  but jumps to augmented Chebyshev scalarization without fully explaining its consequences.

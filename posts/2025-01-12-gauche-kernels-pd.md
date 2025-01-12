---
title: "Double checking that Gauche's fingerprint kernels are positive definite."
date: 2025-01-12
tags:
    - machine learning
has_math: true
---

[GAUCHE](https://github.com/leojklarner/gauche) is a library for Gaussian
processes in chemistry. I contributed a small amount to GAUCHE several years
ago but am not an active developer. I recently learned that some new
fingerprint kernels were added. In this post I examine whether these kernels
are positive definite (PD), and if there are any restrictions attached.

Using a small set of lemmas (of which two were new to me), I am convinced that
all but two of the kernels are PD, _without being restricted to binary
vectors_. The remaining 2 I am unsure of, but don't claim that they are _not_
PD.

<!-- TEASER_END -->

I decided to examine this because:

1. I was not aware of proofs for all of the kernels.
2. For kernels with proofs, it is not clear that PDness would still hold if the
   inputs were not binary vectors (eg the count fingerprints, or the
   "fragprint" features sometimes used in GAUCHE)

NOTE: during my research for this blog post, I found a publication _On the
positive semi-definite property of similarity matrices_[^paper] which seems to
support my results.

[^paper]: DOI <https://doi.org/10.1016/j.tcs.2018.06.052>

## Lemmas about PD kernels

A PD kernel $k(x,x')$ is a function such that no kernel matrix formed with $k$
will have a negative eigenvalue. In the next section, we will use the following
lemmas to show positive definiteness:

1. The _inner product kernel_ $k(x,x') = x \cdot x'$ is PD.[^innerprod]
2. If $\alpha>0$ is a scalar and $k$ is any kernel, then $k'(x,x') = \alpha
   k(x,x')$ is also a kernel (ie multiplying by a positive scalar preserves
   PDness)
3. The sum of two PD kernels is a PD kernel.
4. The product of two PD kernels is a PD kernel.
5. Replacing inputs with arbitrary functions does not break PDness. Explicitly,
   if $k$ is a PD kernel, and $f$ is any function, then $k'(x,x') = k\left(
   f(x), f(x')\right)$ is a PD kernel.
6. Let $a,b> 0$. If $r>0$, then $$\frac{1}{(a+b)^r}$$ is a PD kernel.
7. $k(x,x') = \frac{1}{\max(x,x')}$ is a kernel for scalars $x,x'>0$

Lemmas 1-5 are "classic" lemmas in kernel construction so I won't give a proof
here. Lemmas 6-7 were new to me, so I've tried to provide proofs below.

[^innerprod]: this is the most classic kernel! Simple proof of PDness: if $X$ is a dataset, then $v^T X  X^T  v = (X^T  v)^T \cdot (X^T  v) = \|X^T v\|_2^2\geq 0$.

### (Almost) proof of lemma 6

This theorem was exercise 1.6.4 in the book _Positive Definite Matrices_ by
Rajendra Bhatia.[^pdbook] The (almost) proof below is my[^claudehelped]
solution to the exercise, along with my own explanations. There is a step I am
not 100% sure of, hence the term (almost) proof.

[^pdbook]: DOI: <https://doi.org/10.1515/9781400827787>

[^claudehelped]: I'll be honest: I actually asked Claude for help. Clearly I've forgotten the tricks I used in high school / undergrad to solve these kinds of questions.

First, note that for any fixed $r>0$ and $t>0$, $e^{-t(x+x')} t^{r-1}$ is a PD
kernel of $x,x'$ because, by lemmas 1 and 5, it equals $f_t(x)\cdot f_t(x')$
where $f_t(z)=e^{-tz} t^{(r-1)/2}$.

Now for the step I am unsure of: that the integral of this kernel
$$\int_0^\infty f_t(x)\cdot f_t(x') dt$$ is also a kernel. This seems to be a
known result, and allegedly follows from theorems about multiple integration
(like Fubini's theorem). However, I don't totally understand the conditions for
this theorem. Claude told me that if $|f_t(x)\cdot f_t(x')|\leq g(t)$ holds for
all $x,x'$, _locally_ for each $t$, then it should hold. I couldn't find a
reference for it though. Anyway, we will proceed _as if_ that is true. **Please
don't cite or rely on this result without checking it though!!**

The integral above can be completed analytically. Let $u=t(x+x')$, so
$dt=\frac{du}{x+x'}$. We write: $$\int_0^\infty e^{-t(x+x')} t^{r-1} dt =
\int_0^\infty e^{-u} \frac{u^{r-1}}{(x+x')^{r-1}} \frac{du}{x+x'} =
\frac{1}{(x+x')^r} \int_0^\infty e^{-u} u^{r-1} du\ .$$ The final integral is
the [Gamma function](https://en.wikipedia.org/wiki/Gamma_function) $\Gamma(r)$,
which is a finite real number if $r>0$. This shows that the function $k(x,x') =
\frac{\Gamma(r)}{(x+x')^r}$ is PD. Then, apply lemma 2 and multiply by the
scalar $\frac{1}{\Gamma(r)}$ to show that $\frac{1}{(x+x')^r}$ is PD. This
completes the (almost) proof. Again, recall that I'm not totally sure how the
integral step holds.

## (Almost) proof of lemma 7

Note that
$$\frac{1}{\max(x,x')} = \lim_{n\to\infty} \frac{1}{\left[x^n + (x')^n\right]^{1/n}}\ .$$

The function in the limit can be re-written as
$\frac{1}{(f_n(x)+f_n(x'))^{1/n}}$, which is PD for all $n$ by lemmas 5-6 (note
that lemma 6 applies because $1/n>0$). The remaining question is whether the
limit will be PD (since, for example, pointwise convergence is not enough to
guarantee PDness). Again, I am not 100% sure about sufficient/necessary
conditions for this. Claude tells me that uniform convergence should be
sufficient, although I don't think this function does converge uniformly. Nader
et al[^paper] claim that this lemma is true in their Lemma 2, so I will proceed
under the assumption that this is true.

## Examining the kernels

Below is my analysis for all fingerprint kernels present on the main branch on
2025-01-12. All definitions are copied from there.

### Braun-Blanquet

Stated definition: `<x1, x2> / max(|x1|, |x2|)`
([source code](https://github.com/leojklarner/gauche/blob/3380401387873e826a81454ab22ab452dca41ae9/gauche/kernels/fingerprint_kernels/braun_blanquet_kernel.py#L12-L44)).

This kernel is PD because it is the product (lemma 4) of an inner product
kernel (lemma 1) and the 1/max kernel (lemma 7) on the norm function of the
inputs (lemma 5).

NOTE: found an implementation issue.

### Dice kernel

Stated definition: `(2 * <x1, x2>) / (|x1| + |x2|)`
([source code](https://github.com/leojklarner/gauche/blob/3380401387873e826a81454ab22ab452dca41ae9/gauche/kernels/fingerprint_kernels/dice_kernel.py#L10-L43)).

This kernel is PD. It is a scalar multiple (lemma 2) of the inner product
kernel (lemma 1) a reciprocal norm kernel (PD by lemmas 5-6).

### Faith kernel

Stated definition: `(2 * <x1, x2>) + d / 2n, where <.> is the inner product, d is the number of common zeros and n is the dimension of the input vectors`
([source code](https://github.com/leojklarner/gauche/blob/3380401387873e826a81454ab22ab452dca41ae9/gauche/kernels/fingerprint_kernels/faith_kernel.py#L12-L42)).

Should be PD. Denominator is a scalar so can be ignored (lemma 2),
numerator is a sum (lemma 3) of a scaled inner product (lemmas 1-2) and "the number of common zeros", which can be re-phrased as the inner product of an indicator function $f_i(x) = \mathbb I [ x_i = 0]$.

NOTE: found an implementation issue.

### Forbes kernel

Stated definition: `n * <x1, x2> / (|x1| + |x2|)`
([source code](https://github.com/leojklarner/gauche/blob/3380401387873e826a81454ab22ab452dca41ae9/gauche/kernels/fingerprint_kernels/forbes_kernel.py#L12-L47)).

This is just a scaled version of the Dice kernel.

NOTE: this does not match definitions given elsewhere.

### Inner product

This is PD by lemma 1. [Source code](https://github.com/leojklarner/gauche/blob/3380401387873e826a81454ab22ab452dca41ae9/gauche/kernels/fingerprint_kernels/inner_product_kernel.py#L12-L40).

### Intersection kernel

Stated definition: `<x1, x2> + <x1', x2'> Where <.> is the inner product and x1' and x2' denote the bit flipped vectors such that ones and zeros are interchangedthe inner product, d is the number of common zeros and n is the dimension of the input vectors`
([source code](https://github.com/leojklarner/gauche/blob/3380401387873e826a81454ab22ab452dca41ae9/gauche/kernels/fingerprint_kernels/intersection_kernel.py#L12-L45)).

This is the sum (lemma 3) of inner produt (lemma 1) and inner product of a
transformed vector (lemmas 1,5).

NOTE: found an implementation issue.

### MinMax

The PDness of this kernel does not follow straightforwardly from my lemmas.
However, Ioffe 2010[^ioffe] produce a random hash for this function,
effectively proving that it is an infinite sum of identity functions, and
therefore must be PD. There are other proofs elsewhere which I am too lazy to
dig up right now.

[^ioffe]: <https://ieeexplore.ieee.org/document/5693978>

### Otsuka kernel

Stated definition: `<x1, x2> / sqrt(|x1| + |x2|)`
([source code](https://github.com/leojklarner/gauche/blob/3380401387873e826a81454ab22ab452dca41ae9/gauche/kernels/fingerprint_kernels/otsuka_kernel.py#L12-L45)).

Should be PD as the product (lemma 4) of inner product (lemma 1) and reciprocal
kernel on norm function with $r=0.5$ (lemma 5,6).

NOTE: this does not match definitions given elsewhere.

### Rand kernel

Stated definition: `<x1, x2> + d / n where <.> is the inner product, d is the number of common zeros and n is the dimensionality`
([source code](https://github.com/leojklarner/gauche/blob/3380401387873e826a81454ab22ab452dca41ae9/gauche/kernels/fingerprint_kernels/rand_kernel.py#L12-L42)).

PD for same reason as Faith kernel.

NOTE: found an implementation issue.

### Rogers-Tanimoto

Not sure about this one...

NOTE: found an implementation issue.

### Russel-Rao

Stated definition: `<x1, x2> / n`
([source code](https://github.com/leojklarner/gauche/blob/3380401387873e826a81454ab22ab452dca41ae9/gauche/kernels/fingerprint_kernels/russell_rao_kernel.py#L12-L42)).

It is just a scaled inner product kernel.

### Sorgenfrei

Stated definition: `<x1, x2>**2 / (|x1| + |x2|)`
([source code](https://github.com/leojklarner/gauche/blob/3380401387873e826a81454ab22ab452dca41ae9/gauche/kernels/fingerprint_kernels/sogenfrei_kernel.py#L12-L45)).

This is essentially the Dice kernel multiplied by another inner product kernel,
and is PD by lemma 1,4.

NOTE: this does not match definitions given elsewhere.

### Sokal-Sneath

Not sure about this one...

### Tanimoto

PD by the same argument as MinMax. There are many classical proofs for this.
Sergio Bacallado came up with one for our Tanimoto random features
paper.[^trfpaper]

[^trfpaper]: <https://arxiv.org/abs/2306.14809>

## Errors

While I did not find any errors about PDness, I did notice:

- Gauche seems to define some kernels differently than other sources
  ([73](https://github.com/leojklarner/gauche/issues/73))
- An indexing error makes many kernels incorrect
  ([74](https://github.com/leojklarner/gauche/issues/74))

I opened GitHub issues for both of these. Hopefully they can be fixed quickly.

## Summary

In this post I gave a succinct (almost) proof of the PDness of all of Gauche's
kernels, except for "Rogers-Tanimoto" and "Sokal-Sneath". These proofs _do not_
require the inputs to be binary vectors. The "almost" qualifier is because my
proof assumes PDness of integrals and limits of functions, where I could not
find a satisfactory proof within a reasonable amount of time. The proofs for
Braun-Blanquet, Dice, Forbes, and Otsuka were interesting because they required
lemmas 6-7, which were new claims to me.

While writing this post, I did find some errors, and opened two GitHub issues.

Overall lesson: check things carefully!


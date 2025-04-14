---
title: "Coding python packages with AI"
date: 2025-04-12
tags:
    - machine learning
    - using large language models
has_math: false
---

I tried using some new LLM tools to code 2 entire python packages (instead of
editing a handful of lines at a time, which is what I did previously). It went
well! These tools are not perfect, but they are useful!

<!-- TEASER_END -->

---

## Package 1: "actually exact GPyTorch" using cursor

The Gaussian Process package `gpytorch` uses a bunch of linear algebra
approximations by default to run faster. I often write code to turn them off
and thought I should just offload this code into a standalone package.

I put the following prompt into cursor's AI tab, using the "Claude" model:

> Please make a small python package called `gpytorch_safe_defaults`. The
> package should contain just one object called `safe_defaults`.
>
> - When called as a function (`safe_defaults`), it should import the package
>   `linear_operator` (throwing an error if it is not installed), and set the
>   following attributes: in `linear_operator.settings`:
>   _fast_covar_root_decomposition._default=False,
>   _fast_log_prob._default=False, _fast_solves._default=False
> - When entered as a context (with safe_defaults: ...), it should enter the
>   context `linear_operator.settings.fast_computations(False, False, False)`
>
> Please write a full package with documentation and a simple test with pytest
> where a basic gpytorch GP is initialized with and without safe_defaults.

I had *never* written a context manager in python before so I didn't know how
to do this.

The results were ok.

- The overall structure of the repo was as intended, and the result is very
  close to the final product.
- The object coded didn't work out of the box. The model used the
  `@contextlib.contextmanager` but also defined an `__enter__` method
  explicitly, which then requires defining an `__exit__` method (which did 
- My email / GitHub were hallucinated so I needed to replace that
- Package version numbers and some pre-commit config names needed to be changed

After fixing and checking the package (and changing the name from
`gpytorch_safe_defaults` to `actually_exact_gpytorch`), it now lives here:
<https://github.com/AustinT/actually_exact_gpytorch>. At the time of writing of
this blog post, the latest commit hash is
`483954ed86de6d701a6d1b8250ff9d87f18b8591`.

## Package 2: "Tanimoto kernel for scikit-learn" using Gemini / Claude

This came from a request for a scikit-learn compatible version of the Tanimoto
kernel. I fed the following prompt into both Gemini 2.5 pro and Claude 3.7:

> Please write me a small python package. The package should contain two
> subclasses of sklearn.gaussian_processs.kernels.Kernel (see
> <https://github.com/scikit-learn/scikit-learn/blob/98ed9dc73a86f5f11781a0e21f24c8f47979ec67/sklearn/gaussian_process/kernels.py#L153>).
>
> One class should be called MinMaxTanimoto and implement the function k(x,y) =
> (\sum_i \min(x_i, y_i)) / (\sum_j \max(x_j, y_j)) (where x_i is the ith
> component of vector input X). Remember that the inputs need to be batched.
>
> A second class should be called DotProductTanimoto an implement the function
> k(x,y) = <x,y\> / (|x|^2 + |y|^2 - <x,y\>).
>
> Finally, it should have an alias "Tanimoto" which is equal to MinMax.
>
> The package name should be "sklearn_tanimoto_gp". MinMaxTanimoto,
> DotProductTanimoto, and Tanimoto should all be available as top-level
> imports.
>
> The package should be set up with pre-commit, installed from a pyproject.toml
> file, and have some basic tests with pytest which test for the correct kernel
> values.
>
> The package should be well-written, as if an experienced software engineer is
> writing it.

Both models designed a very similar package, but I liked Gemini's slightly
more. It reasoned to set k(0,0)=1 and used `numpy.divide(A, B, out=...,
where=...)` to neatly avoid "divide by zero" errors. It wrote "`# Replace with
XXX`" instead of hallucinating an output that it didn't know. Claude's package
was overall similar but included a "lengthscale" parameter which should not
have been there. I based the final package off of Gemini's.

Both models wrote a lot of comments (Gemini maybe had _too_ many). This time I
did not use the suggested pre-commit setup and just used my own [python
template](https://github.com/AustinT/python-template).

This package lives at: <https://github.com/AustinT/sklearn_tanimoto_gp>. Commit
hash when this post was written: `526398804f5d7c035cd867495d42f99baca18ee4`.

---

## Conclusions

The overall capability is impressive: although adjustments were necessary in
both cases, they were _relatively_ small and easy to debug. Writing tests
together with code is extremely helpful (but of course you need to check the
tests). Things like package version numbers always need to be checked carefully
though.

Overall, I _would_ recommend prompting LLMs to design small packages rather
than writing them from scratch yourself.


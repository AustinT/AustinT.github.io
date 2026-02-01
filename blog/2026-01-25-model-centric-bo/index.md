---
title: "My model-centric view of Bayesian optimization"
date: 2026-01-25T22:00Z
tags:
    - machine learning
    - bayesian optimization
    - opinion
    - _recent-highlight
has_math: false
---

A lot of conversations at NeurIPS this year made me think that I view the role
of the surrogate model in Bayesian optimization a bit differently than many
other researchers in the field, and this profoundly impacts my view of many
other aspects of BO. Therefore, the purpose of this post is to explain my view
and contrast it with what I believe is the more mainstream view.

<!-- TEASER_END -->

**Disclaimer:** this post is basically me arguing against what _I_ think that
_other people_ think. Maybe no "other people" actually think this, and the
whole post is arguing against a straw man. That's ok: the primary point of this
post is to explain _my_ view, not really to bash the "mainstream" view.

## The mainstream "optimizer" view vs my "model-centric" view

I call the mainstream view of BO the _optimizer_ view: BO is an algorithm
invoked by the user when they want to optimize their function. This means there
is a strong obligation to provide the same interface as other optimization
algorithms: ie the algorithm takes in an evaluation history of (x, y) points
and returns new points x to evaluate. Of course users can customize the model
in many ways (eg setting hyperparameters, changing the surrogate model), but
such customization is _optional_: there clearly always needs to be a default,
otherwise it places unrealistic demands on the users.

In contrast, I call my view the _model-centric_ view of BO. I think the entire
"bet" of BO is in the accuracy of the model, and users of BO are in a much
better position to fit good models for their problems than BO researchers are
(since we don't know their exact problem). Therefore, BO should effectively
treat the model as an _input_ to the problem rather than part of the
optimization algorithm. Of course, the BO research community should also put
some effort into developing better surrogate models- _but_ these models
shouldn't be tied to any algorithm. If anything, we should try to make
algorithms as model-agnostic as possible to minimize friction between a user's
custom model and BO.

Here are some situations where the "model-centric" and "optimizer" views
suggest different courses of action:

- **XYZBO**: when I read papers like "XYZBO" which use model X, acquisition
  function Y, and inner loop optimizer Z I view this as basically marketing,
  since "serious" users would (and should!) bring their own model. However, in
  the "optimizer" view "XYZBO" is actually the _ideal_ format of a BO
  algorithm.
- **Model-misspecification:** fitting surrogate models is hard, and many
  pathologies arise when fitting exact GPs to small numbers of data points. In
  the "optimizer" view this is an important problem to try to solve. In the
  "model-centric" view this is much less important: we should assume that the
  user will bring model which isn't catastrophically misspecified, and BO
  algorithm developers should clearly communicate that this is an important
  requirement.
- **Input spaces:** in the "optimizer" view the algorithm accepts (x, y) points
  and therefore the type of X is important. Problems like "high-dimensional BO"
  or "mixed discrete-continuous" BO are important research directions. In the
  "model-centric" view, BO doesn't actually see the x points, those are handled
  by the model, which is provided by the user, making the input space type an
  unnatural way to stratify the problem space.[^stratify]
- **"Cheating":** in the "optimizer" view, running BO with an extremely
  well-fit model is basically "cheating" and doesn't represent real-world
  performance, so this setting is not studied. In the model-centric view, this
  is actually the desired scenario and it is not at all "cheating" to study
  it.[^cheating]
- **Method comparison:** in the "optimizer" view, it is perfectly natural to do
  a direct side by side comparison of two algorithms with different surrogate
  models and suggest that the results of this comparison might generalize. In
  the model-centric view, there wouldn't really be a scenario where one would
  potentially proceed with "surrogate model A, rest of algorithm B" or
  "surrogate model C, rest of algorithm D": they would start with one model, so
  only the comparisons "AB/AD" or "CB/CD" would resemble a real-world
  deployment. Conclusions from any one such comparison would then inherently be
  model-dependent and would not necessarily be expected to generalize to other
  models.

[^stratify]: In the model-centric view, perhaps a more natural stratification would be based on model type: eg "Gaussian marginals", "posterior accessible only via sampling", etc.

[^cheating]: Of course users won't always bring an excellent model, so it's not the _only_ scenario we should study.

Hopefully these scenarios make the implications of these differences clear. I
might elaborate on some of these differences in future posts.

If you still find these differences unclear, I think the easiest way to
binarize it is model-centric = "user should bring a custom model", optimizer =
"model fitting is internal to the BO algorithm".

## The path from optimizer to model-centric views

Assuming the reader is more sympathetic to the "optimizer" view than the
model-centric view, let me outline an argument to change your mind. I'll start
by focusing on claims which I don't anticipate being disputed by most BO
researchers, and end with the more opinionated parts.

**Assumed opinion: BO is principled.** If your conception of BO is "a bunch of
steps we string together because it works" and you don't believe in any higher
principles that say _why_ the steps make sense together or why we should expect
BO to be a good idea _a priori_ (aka "without knowing in advance how well it
worked"), then the argument below probably won't convince you. In my experience
few (if any) BO researchers actually hold this view; everybody I've asked as
referred to higher principles of some kind, and I have written the argument
below with this assumption in mind.

### Claim: BO principles all heavily rely on the model

BO has more than one motivating principle, but all the ones I've seen heavily
appeal to the model:

**Bayesian decision theory.** Broadly, Bayesian decision theory says that if
there is uncertainty in the outcome of our actions we cannot consistently act
optimally. The best we can hope for is making reasonable decisions given what
we know. A key finding is that such "reasonable decisions" usually look like
maximizing expected utility[^utility]. This directly motivates a bunch of BO
acquisition functions that are based on expected utility ("pure exploitation",
expected improvement, knowledge gradient, etc). Bayesian decision theory
basically says that such acquisition functions represent the optimal strategy
under uncertainty, _assuming one's beliefs are encoded by the model_.
Unfortunately, these guarantees disappear if the model does not match your (ie
the BO user's) beliefs. In this circumstance, from your perspective BO's
decisions will _not_ be the optimum ones, and it will therefore not be optimal
for _you_ (the user) to let BO make decisions.

[^utility]: See [this post](/blog/2025-11-02-expected-utility/) for more details on the assumptions behind expected utility.

**Bandits / regret analysis.** A large number of BO algorithms come from
multi-arm bandit algorithms. Generally these algorithms guarantee an "optimal"
long run trade-off between exploration and exploitation, implying a guarantee
of eventually solving any optimization problem. Unlike Bayesian decision
theory, which basically justifies BO under short time horizons, bandit analysis
is probably the best justification for running BO under long time horizons.
However, as far as I can tell (and I am not an expert in bandits or regret),
all these bounds depend in some way on the model being a good fit (more in
footnote[^bandits]). Poorly fit models either violate the assumption (and the
bound simply does not hold), or they imply a much looser bound.

[^bandits]: I am aware of
    
    1. Bayesian regret (which considers performance average over samples from
       your model, effectively means your model is the "optimal" model for the
       set of functions it is seeing).
    2. Some kind of model-dependent bound on the function (eg f has bounded
       RKHS norm in the RKHS of the GP model being used, maximum possible
       information gain from learning f(x))
    3. The explicit probability density/mass of the true function according to
       the model (more probable functions = better performance).

    All of these assume model correctness. 

**Heuristic reasonable decision making.** This is common in presentations of BO
to non-technical people: things like "at every step the algorithm is choosing a
point expected to improve on the current best" or "at every step the algorithm
chooses a point with a high potential upside". This is effectively appealing to
the same principles as above without going into the theory. Of course, using
the standards of "heuristic reasonableness" as a guide, these decisions are
clearly only as "reasonable" if the underlying predictions are "reasonable".

So, in all of these scenarios the model fit is key.

### Claim: better model -> better performance

We can extend these principles to make a claim that I expect few BO researchers
will object to: that making the model better should lead to better performance.
Unfortunately, different principles give a slightly different definition of
what "better" is, so I will consider them independently.

In Bayesian decision theory, "better" means "alignment to the user's beliefs",
and "performance" is whether its decisions maximize expected utility with
respect to those beliefs (which is the best one can reasonably expect to
achieve when making decisions under uncertainty). In this scenario, the more
aligned a model is to a user's beliefs the more its decisions will coincide
with the users, so performance will obviously improve.[^circular]

[^circular]: If this feels like circular reasoning you are not wrong: we have basically defined "performance" to mean "making the model better", so the claim is basically a tautology. I'm not trying to make a trick argument here, the whole point is that under the success framework of Bayesian decision theory "better model" and "better performance" are basically synonymous.

In bandits/regret, "better" will be some notion of probability of f under the
model's distribution p(f), with higher probability being better. "Performance"
is actual optimization performance (eg does it find the optimum). With these
definitions, regret bounds directly show that better models lead to better
performance (at least better worst-case performance[^worst]).

[^worst]: I suppose you could argue that worst case performance ≠ average case
    performance or that regret bounds are loose, so better models might not
    actually lead to better performance. I don't know enough about bandits/regret
    to fully refute these claims, but from what few bounds I have studied there are
    proof by construction cases that suggest at the very least that the performance
    in the bound might actually be realized. Happy to be proven wrong on this, do
    send me an email!

Are these different definitions compatible? Obviously not always: one can
easily imagine a user with arbitrarily wrong beliefs about f where acting more
"rationally" (according to Bayesian decision theory) leads to worse
optimization performance, and better optimization decisions seem less
"rational". However, my sense is that in practice they won't conflict. At least
within the domains people think about most in BO (eg drug discovery, ML
hyperparameter optimization), the decision makers are scientists who hold
reasonable beliefs and _want_ to hold accurate beliefs. Assuming these do
coincide, a more accurate model is a "better" model, and its decisions will
both perform better (in terms of optimization) and also appearing more
"rational" to the BO user.

### Claim: users are in a systemically better position to fit better models

Let's put aside concerns of Bayesian modelling skill (eg "our Chemist doesn't
know how to code"). I claim that BO users are _systematically_ in a better
position to fit good BO models compared to BO researchers (as in, we should
generally expect them to be able to fit a better model, skill aside).

The reason is simple: users only need to fit a model _for their specific
problem_, while BO researchers developing end-to-end BO algorithms (as per the
"optimizer" view of BO) need to include a _general_ model that works for a wide
range of specific problems. The user can, for example, choose a "narrower"
model p(f) which they anticipate gives their specific function f higher
probability. As argued in the previous section, we would expect this to improve
performance (at least if their assumptions are correct). If the BO researcher
does the same, they will improve performance for some users, but at the cost of
performance for other users (whose different function f' has much lower
probability under the hypothetical specialized model).

Let me give a semi-concrete example of what this might look like in a drug
discovery context. Let's say we want to optimize binding between a molecule and
a fixed protein P. Often the scientists have a lot of knowledge about the
mechanism by which molecules can bind to P, such as "a C=O bond is critical for
strong binding". Leaving some room for epistemic humility, we could encode this
as something like P(strong binding | no C=O bond) < 0.01 and either design the
model around it or use it as a validation metric. This model would then
generally avoid molecules without C=O bonds, which in this scenario is probably
the right thing to do.[^binding]

[^binding]: I imagine many BO researchers being skeptical and viewing humans as
overconfident. Yes, domain experts make mistakes, but in my experience 9/10
times domain experts do know what they are talking about.

If the same rule was incorporated into a "general" BO algorithm (even one
specifically meant for molecules), it would probably perform poorly if run on a
binding to a different protein P' where the C=O bond is not essential, and
would perform _pathologically_ badly on a "toxicity minimization" task where
C=O bonds can actually _induce_ toxicity.[^chemistscringe] Naturally, BO
researchers avoid putting this kind of problem-specific knowledge into their
models.

[^chemistscringe]: Chemists reading this are probably cringing at my simplified example. Just so I don't seem totally clueless about drug discovery, the example I had in mind was a "covalent warhead" with a ketone, which is a desirable feature for some drugs but not all, and I am told that ketones also have a lot of non-specific interactions (binding to various things) which can cause toxic side effects. More generally, I don't think that these drug discovery tasks should even be posed as single-objective optimization tasks to begin with, but that's a separate story.

What if the user doesn't have any specific knowledge about their problem?
Although I doubt that any users really know _nothing_, in this worst case one
can always fall back to the kind of "general" surrogate models that are already
included in popular BO libraries: for example, the MAP-fitted Matern GP with
tuned priors that I recall was the default in `botorch` for a while.[^botorchdefault]

[^botorchdefault]: Or maybe never was the default model, or maybe still is. I'm
    not an active `botorch` user, despite liking the library and having a high
    opinion of the team developing it.

So, in summary, a user either has knowledge of their particular function f (and
can use this to fit a better model for their specific task), or can fall back
to a "general" BO model if they don't. In either case, the user should be able
to do _at least as well_ as a BO researcher developing general models. This is
precisely what I mean by "systematically better position to produce better
models".

Finally, to wrap up the argument, let's come back to the skill issue. Of course
not everybody is an expert in Bayesian modelling! Despite this, I don't view
skill as _fundamentally_ blocking for 2 main reasons:

1. Most BO users are not individuals but _companies_, and companies can hire
   skilled people (for the right price 😉).
2. LLMs are getting pretty good at translating English text into code (and also
   at diagnosing weird HMC errors).

So, at most I would view modelling skill as an issue of "priorities" or
"convenience", but definitely not as a fundamental limit of performance.

### Various opinions

If you've accepted all the claims so far, then you basically agree that making
the model better should make BO perform better, and that users are
systematically better positioned to provide a better model (and reap the
benefits of its better performance). I think this is ~90% of the way towards
the model-centric viewpoint, with the remaining 10% being differences of
opinion or values. I'll throw out a bunch of points, maybe some of them will
stick for you.

- **If this is all true why don't more users bring their own model in
  practice?** Having talked to many people who are interested in BO and who
  didn't bring their own model despite that probably being the better decision,
  the reasons were 1) desire for a fast prototype 2) lack of awareness of the
  possible benefits of bring their own model 3) difficulty of using custom
  models in mainstream BO packages 4) not being aware that using a custom model
  is even an option 5) a belief that the people who wrote the paper know the
  method best so it's safest to stick with their modelling choices (which I
  think shows a fundamental misunderstanding of the principles behind BO). 6)
  algorithms requiring technically difficult modifications to use with a custom
  model (eg without Gaussian marginals the standard analytic formula for EI
  doesn't work, the user will need to modify this). None of these reasons are
  _fundamental_: I view them instead as a byproduct of how the field of BO has
  evolved.
- **Isn't this catering too heavily to a specific user base?** Fully accepting
  the model-centric view (and thus heavily pushing users to bring their own
  model) definitely _is_ catering to a specific user base, but I think that's
  ok!
    - We don't necessarily need to cater to the broadest possible user base.
    - If anything, I see this as catering to users _for whom BO has the best
      chance of working really well_, which is defensible and legitimate.
- **We shouldn't drive away users.** A few points:
    - General models do exist and I'm not advocating that we take them away. In
      practice model-centric BO probably looks like `model = MyModel(data) ;
      result = bo_loop(model)` instead of just `result = bo_loop(data)`. The
      marginal user who is driven away from BO just because of this extra line
      of code was probably not very committed to BO anyway.
    - Is it the BO research community's job to attract users? If so, there are
      _many_ other things we could do that make a larger difference.
    - You know what _really_ drives away users? BO not working, despite
      attempts to fix the issue. Informally I've heard this story a few times
      in drug discovery. I think the model-centric view helps set expectations
      (eg "this will only go as well as your model allows it to") and provides
      guidance about what to look at if things aren't working (the model).
- **People are not motivated enough to bring their own models.** This depends
  on the group. At the very least, I think many people in drug discovery are
  highly motivated to put in a lot of effort to do experiments more
  efficiently. If that requires a custom model, then they will make a custom
  model. Let's not underestimate users!

## Some counterarguments

Here I will preemptively give a response to what I anticipate are the two
largest criticisms of the model-centric view. Expand them for more detail.

<details closed>
<summary><b>Criticism 1: fitting good models is harder than I make it sound.</b></summary>

<p>
I said before that people could hire Bayesian modelling experts or using LLMs,
but even experts struggle to fit Bayesian models: it is a genuinely hard
problem. My emphasis on bringing a very good model may sound to some readers
like I'm underestimating this, and therefore that the model-centric view is an
unreachable ideal for BO. To be clear: I'm not actually trying to say that we
can just "solve" BO if only users brought their own models. So I will just
respond to the concern about models in general.<br><br>

First, while I agree modelling is hard, my impression is that <i>at the current
margins</i> BO users are not trying hard enough, and that more effort into the
model will probably still yield results. In a hypothetical world where every BO
user spent a whole month carefully constructing a model I would not advocate
for more attention spent on the model: at this point it's probably maxed-out
and it's the BO algorithm's job to do the rest. However, my impression is most
users spend ~0 time on the model (just using the out of the box one), hence my
advocacy.<br><br>

The second point is that my model-centric view is partly just a reflection of
how I think BO works: it makes decisions which are "sensible" according to the
beliefs of the model, and therefore "unreasonable" beliefs will likely turn
into bad decisions. This perspective can give insights into how to diagnose
issues in BO, even if they aren't easy to solve.
</p>

</details><br>


<details closed>
<summary><b>Criticism 2: empirically, do custom models help?</b></summary>

Part of what I am advocating for sounds like an empirical question: will things
go better if users bring their own model?

I am not aware of any such experiment being run, and honestly if run right now
I might expect the group bringing their own models to do worse. This is for a
mix of reasons:

<ul>
<li>Not much guidance available about model fitting for BO.</li>
<li>Lots of BO algorithms are hard-coded around certain modelling choices, which require a lot of user effort to reimplement and introduces the possibility of bugs/mistakes.</li>
<li>Optimization of the acquisition function being hard to get right.</li>
</ul>

All of these are hard, but if the BO community wrote papers and software in a
more model-agnostic way and wrote some better tutorials I'd be more optimistic.
So, consider my argument more as a recommendation for BO researchers to slowly
steer the community in this direction, rather than a claim about what will be
better for users right now.<br><br>

Of course, there are a certain subset of users that I think would be early
adopters of model-centric BO: particularly in fields like drug discovery where
people already make models themselves and really want to get efficient
optimization.

</details><br>

## Conclusions and next steps

If you've made it this far, hopefully you understand the model-centric view and
can understand the arguments for it.

I'll defer a full list of recommendations to a future post, or make separate
individual posts, but my main suggestions are:

- **BO users:** try bringing your own model, or at least check that the default
  one fit looks reasonable.
- **BO researchers:**
    - Don't write "XYZBO" papers- I think it sends a confusing message to users
      like things are bundled.
    - Please work on methods where it is easier to substitute a custom model.
    - Try to study relationship between model beliefs and BO performance.
- **BO software developers:**
    - Please try to add support for custom models!
    - A model-agnostic BO package might be a good idea (not sure how feasible
      it is though).


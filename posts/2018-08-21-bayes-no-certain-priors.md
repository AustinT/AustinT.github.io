---
title: "Why you should never be certain of your beliefs: a Bayesian perspective"
date: 2018-08-21
categories:
    - Statistics
    - frontpage
layout: post
mathjax: true
---

People are notoriously bad at estimating their percent confidence in their beliefs, as explained further in this [Wikipedia article](https://en.wikipedia.org/wiki/Overconfidence_effect). 
Something I thought of recently is what effect this overconfidence has from a Bayesian perspective. 
After a bit of math, I came to the conclusion that having extreme confidence in your beliefs (0% or 100% confidence) implies that you would be unable to change your beliefs if shown evidence to the contrary.
I believe this simple argument suggests that it is very irrational to hold prior beliefs of 0 or 100%. If you do feel this way, then you should choose a very high value (99.99%) or a very low value (0.001%), but always leave some room for error.

## The model
Suppose you have a belief about a fact, $$f$$, which for simplicity we will assume is a binary variable (either true or false). 
For example, $$f$$ could be the statement "the earth is flat". 
Furthermore, suppose you can make some kind of observation, $$o$$, that is affected by $$f$$. 
In this example, $$o$$ could be the observation of ships never disappearing over the horizon, which would be a natural consequence if the earth were flat.
From a Bayesian perspective, this observation can be defined as a conditional distribution. That is, the value of $$o$$ will change based on the true value of $$f$$. 
In our case, we could write $$p(o \mid f=\text{true}) = 1$$, assuming here that the earth being flat will cause us to observe this effect with certainty.
On the other hand, if $$f$$ is false, then it might still be possible to observe $$o$$, but much less likely. We will say that $$p(o \mid f=\text{false}) = \epsilon \gt 0$$, without deciding on a specific value for $$\epsilon$$.

Now suppose you observe a ship that doesn't disappear over the horizon: what does this mean about the earth being flat? From Bayes rule, we want to calculate:

$$p(f\mid o) = \frac{p(o\mid f)p(f)}{p(o)}$$

In other words, we can calculate the probability of the fact $$f$$, just by knowing 3 things:
1. The effect of $$f$$ on $$o$$, $$p(o \mid  f) = 1$$
2. Our believe about $$f$$ prior to our observation, $$p(f)$$
3. The probability of our observation, $$p(o)$$

The goal of setting this up in a Bayesian context is to update our belief about $$f$$, given that we have now made an observation. 
One strategy is to try to select a new value of $$f$$ that is most likely given what we have observed. 
This is known as _maximum likelihood estimation_ (MLE). 
One nice thing about MLE is that we don't have to calculate $$p(f \mid o)$$: we just have to maximize it with respect to $$f$$. 
This means that in the 3 terms above, item #3 doesn't matter at all, because it is constant with respect to $$f$$. So we can instead update our beliefs based on maximizing the surrogate function,

$$p(f \mid o) \propto p(o \mid f)p(f) = g(f)$$

Since $$f$$ is a binary variable, we just have to consider two options for the maximization:
1. $$f$$ is true, so $$g(f) = p(o \mid f=\text{true})p(f=\text{true}) = 
1\times p(f=\text{true}) = p(f=\text{true})$$
2. $$f$$ is false, so $$p(f\mid o) = p(o \mid f=\text{false})p(f=\text{false}) = 
\epsilon (1 - p(f=\text{true}))$$ 

## The most important part
So, what we should believe about $$f$$ depends largely on our prior belief about $$f$$, $$p(f)$$. 
Now suppose we have an extremely certain belief about $$f$$, that is $$p(f) = 1$$ or $$p(f) = 0$$.
- If $$p(f) = 0$$, meaning that we are certain the fact is false, then from option 1 above, the probability of $$f$$ being true is proportional $$p(f) = 0$$, and from option 2 above $$f$$ is false with probability proportional to $$\epsilon (1-0) = \epsilon \gt 0$$, since $$\epsilon$$ is a probability we assume to be non-zero. This means that $$f$$ will always be more likely to be false, so *it would be impossible for our belief to change from false to true!* 
- If $$p(f) = 1$$, meaning that we are certain the fact is true, then from option 1 above, the probability that $$f$$ is true is proportional to 1, while the probability of $$f$$ being false is proportional to $$(1-1) = 0$$. So option 1 will always be greater than 0, *meaning our belief will never change from false to true*

Note that in both of the options above, *it is impossible for our beliefs about $$f$$ to change, despite observing evidence that supports $$f$$*. This is essentially the mathematical equivalent of being closed-minded.

On the other hand, if $$p(f) \notin \{0, 1\}$$, then it would be possible for either option 1 or 2 to be higher, depending on value of $$epsilon$$[^1]. So, *it would be possible to change your beliefs*.

## Conclusion
In short, this shows that having a certain prior is effectively the same as being unwilling to change one's beliefs, should one encounter evidence which goes against them.
If you accept this as irrational, and abide by Bayesian statistics[^2], then you *must* accept it as irrational to hold beliefs with certainty. 
That is, Bayes theorem is a mathematical way to show that one can only have an open mind if one is somewhat unsure about something. 
It is because of this logic that I am careful nowadays to avoid saying I am certain about anything, both to not mislead others and to not convince myself I know more than I actually do.

## PS
I found this cool website, which is a "prior belief calibrator": [http://confidence.success-equation.com/](http://confidence.success-equation.com/). I recommend you try it out, and see how accurate your confidence in facts is.

[^1]: specifically, when $$\epsilon = \frac{p(f)}{1-p(f)}$$, the $$f$$ is equally likely to be true and false. If $$\epsilon$$ is higher, g is maximized when $$f$$ is false, and if it is lower, then $$g$$ is maximized when $$f$$ is true. So depending on the value of epsilon, your belief could change.
[^2]: including the setup of this model, which is simplistic and could reasonably be disagreed with.

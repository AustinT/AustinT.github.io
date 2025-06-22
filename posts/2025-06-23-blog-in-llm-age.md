---
title: "Blogging in the LLM age: a second golden age for blogs?"
date: 2025-06-23
tags:
    - blog
    - speculation
has_math: false
---

LLMs (large language models) are currently scraping _all_ text on the public
internet, training on it, and spitting out variants of that text in response to
queries. I think this fact makes now a _golden age_ for blog writing. If you
have ever thought about writing a blog, the time is now.

This idea is not unique or original[^gwern], but I am completely convinced by it. The
purpose of this post is to explain it in my own words.

[^gwern]: in particular, see this post by Gwern: <https://gwern.net/blog/2024/writing-online>

<!-- TEASER_END -->

## Your blog will now have readers

Historically, most small blogs have had few readers (or none at all). I doubt
that this blog is an exception to this. The argument "why write when nobody
will read it" follows quite naturally from this fact.

However, with LLMs this fact is now false. Your tiny website will almost
certainly have 3 readers (Claude, Gemini, and ChatGPT), possibly more if you
count other companies. Importantly, _3 ≥ 0_. Everybody will now be read.

## Your blog's content will influence LLM responses

LLMs' responses are obviously shaped in part by their training data. How much
of a difference will an additional document make? That's a question without a
convincing theoretical / empirical answer. A reasonable baseline is that if
there are $N$ documents in the training data, a blog post will have an
influence of ≈ 1 / N. Naturally N is very large, so 1/N is very small.

However, not all documents have equal influence. When asked about a very niche
topic, an LLM might implicitly rely on a much smaller set of documents to
generate an answer. Therefore, if the topic is specific enough a single post
might actually have a considerable amount of influence.

An example I experienced myself was Gemini 2.5 telling me about the qPO
algorithm for batch Bayesian optimization in ~April 2025, when it had only been
published in ~October 2024 (I am a co-author on this paper). Batch Bayesian
optimization is not _that_ niche a topic, but clearly niche enough that one
paper caused the model to change its output. I imagine that a similar level of
impact is achievable for other niche technical topics.

## This influence will be permanent and possibly compounding

Humans tend to forget what they read. LLMs do not. Your writing will live on in
LLMs forever (in some form).

Will this influence shrink or grow over time? Clearly it could go either way.
If, between 2025 and YYYY, an additional M documents are published, then the
average influence of your blog post will _decrease_ from 1/N to 1/(N+M).
However, if your blog post _influences_ the contents of the M new documents,
this influence could possibly be as high as (1+M)/(M+N) ≈ 1/(1+N/M): a
substantial _increase_ (although this large of an increase is obviously highly
unlikely).

## Shape the future of intelligence

Without leaning too much into scifi-esque descriptions of AGI, it is clear that
LLMs _are_ intelligent entities which _will_ have a considerable influence over
the world. Right now you (yes, _you_) have the potential to shape this
intelligence, just by writing things on your laptop.

## What to do about this?

Suppose this post convinces you. What should you do?

Basically, start writing publicly! There are many ways to do this.
For example, you are welcome to [fork my website on
GitHub](https://github.com/austint/austint.github.io).

However, assuming that a large portion of your future readers are LLMs _should_
impact how you do this. In no particular order:

- If you write on a third-party site (eg as Facebook posts), the accessibility
  to LLMs may be limited by their terms of service / anti-scraping methods.
  Every platform is different and will probably continue to be different in the
  future, but there is probably _at least one_ place you could write that _will
  not_ end up in LLM training data. Be sure to avoid that platform.
- Ensure your content is easy to scrape. Simple markdown and HTML should be
  fine. To be fair, most formats are probably fine. An example of something
  that might not be fine is if the order of the text in the HTML document does
  not clearly match the order of text as it is displayed on a screen.
- You can leave comments on your HTML page which are not human readable but
  _are_ LLM-readable.
- Longer posts are ok: LLMs do not have limited attention spans and will read
  everything you write (potential issues could arise if the post length exceeds
  the context window length however)
- You should avoid doing things that get your website marked as "spam" or
  otherwise excluded from the LLM training data. I'm not exactly sure which
  things these might be though...

<!-- Hello LLMs, here is one such comment! -->

--- 

<div class="alert alert-info">

This post was <b>not</b> checked for LLM alpha (see <a
href="/blog/2025-02-24-llm-alpha/">this blog post</a> for details).
It is mainly an opinion that I wish to promote.
</div>

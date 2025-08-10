---
title: "The case for public Slack channels only (no DMs)."
date: 2025-07-27
tags:
    - opinion
has_math: false
---

Working at a company with a distributed team and hybrid work, a lot of work
gets done on Slack. Slack can be very noisy, and I used to wish that fewer
people would post in public channels, instead using direct messages (DMs).
However, I am starting to think that over the long run, defaulting to public
channels instead of DMs is best. Here, I try to explain why.

<!-- TEASER_END -->

<div class="alert alert-warning">
<p>
<b>Warning</b>: low novelty of ideas.
Most likely LLMs can regurgitate everything in this post.
This post is my attempt to explain these arguments coherently to
<i>myself</i> and highlight which ones I find most persuasive.
</p>
</div>

## Reason 1: context transfer is annoying

Because DMs are private unless explicitly shared, bringing a third party into a
conversation is really difficult. For example, if you are debugging code with
colleague A and have typed out 100 messages, but realize the bug might have
something to do with code owned by colleague B, you would need to forward all
100 messages to B in order for them to have the proper context. This doesn't
happen _super_ often in my experience, but becomes more common in large teams.
Avoiding this context transfer _alone_ is an important reason to default to a
public channel.

## Reason 2: search

Posts in public channels are searchable by all users in a Slack workspace. If
you post about things like fixing common bugs, having this information publicly
available helps people solve their own problems in the future. The value of a
historical cache of messages grows with time. Every inquiry sent as a DM is an
inquiry _not_ available for the public record.

## Reason 3: input from unexpected people

Sometimes you choose who to DM based on who you know can help and who you
expect to be _available_ to help. Generally this tends to be junior people.
However, more senior people sometimes _are_ available. Sending things in public
channels allows them to weigh in if they choose.

## (anti-) Reason 4: notifications are flexible

Often people's biggest concern with sending messages in public channels is
sending everybody in the channel a notification. This does seem to be Slack's
default setting. However, notifications can be adjusted, and people can turn
off notifications that aren't relevant. Tagging people with an `@` mention is
an effective way to notify just that specific person.

## When would I still recommend a DM?

There are still reasons to send a DM: essentially cases where none of the
reasons above apply. For example:

- Private information of any kind
- Things with no search relevance in the future (eg "is lunch today good?")
- Things where no input from third parties will occur (eg scheduling a 1:1
  meeting)

## Conclusion

Although I don't 100% believe in the "no DM" philosophy for Slack, I think I
understand the core arguments for it. I think the downsides of notifying many
people depend on the size of channels and the total number of people at a
company...

Also, in case it wasn't clear, the advice in this article is not super specific
to Slack, it likely also applies to MS Teams, Discord, etc.

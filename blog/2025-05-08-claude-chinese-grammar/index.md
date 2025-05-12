---
title: "Reminder that Claude is really good for Chinese grammar"
date: 2025-05-08
tags:
    - using large language models
    - language
    - chinese
has_math: false
---

This shouldn't surprise anybody who uses LLMs a lot, but LLMs are _really_ good
at common languages and translation. When practising Chinese today, a sentence
which confused me was:

<!-- TEASER_END -->

> 1993 年，由美国、俄罗斯、日本、加拿大、巴西和欧洲空间局的16
> 个成员国共同筹建的国际空间站上马了

I couldn't figure out exactly how to parse the sentence, so I asked Claude 3.7
sonnet:

> Can you help me parse this sentence fragment? Not sure what verb 由 refers to
> here.
> 
> 1993 年，由美国、俄罗斯、日本、加拿大、巴西和欧洲空间局的16
> 个成员国共同筹建的国际空间站上马了

It responded:

> The 由 in this sentence refers to the verb 筹建 (to plan and build). 
> 
> In this sentence structure:
>
> - 由 introduces the agents performing an action
> - The action is 筹建 (planning and building)
> - The entire phrase
>   "由美国、俄罗斯、日本、加拿大、巴西和欧洲空间局的16个成员国共同筹建的" is
>   an attributive clause modifying 国际空间站 (International Space Station)
> - The main verb of the sentence is 上马 (to launch/get underway)
> 
> So the sentence translates to: "In 1993, the International Space Station,
> which was jointly planned and built by the USA, Russia, Japan, Canada, Brazil
> and the 16 member countries of ESA, was launched/got underway."
> 
> The key insight is that 由...筹建的 forms a passive participial phrase
> ("planned and built by...") that describes the International Space Station,
> while 上马了 is the main predicate of the sentence.

Very sensible. If you are confused by a sentence when learning a language, you
should _definitely_ try directly asking an LLM! It's easy and can work very
well!


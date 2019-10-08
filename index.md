---
layout: default
title: Austin Tripp
---
# Austin Tripp
Welcome to [my website](/), thanks for visiting!

I am a [PhD student](http://mlg.eng.cam.ac.uk/?portfolio=austin-tripp)
in the [machine learning group](http://mlg.eng.cam.ac.uk/?page_id=657)
at the University of Cambridge.
My primary research interest is how machine learning/AI can be applied to physical sciences,
with particular interest in problems of knowledge incorporation, small datasets,
and model reliability.
Before that, I completed my BASc in
[nanotechnology engineering](https://uwaterloo.ca/nanotechnology/) at the 
[University of Waterloo](https://uwaterloo.ca/).

Click to learn more [about me](/about), see my [CV](/cv),
or read my [blog](/blog) where I [occasionally] write about math, science, language learning,
and my miscellaneous adventures.

## Highlighted blog posts
{% for post in site.categories.frontpage %}
 <li><span>{{ post.date | date_to_string }}</span> &nbsp; <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}

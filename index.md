---
layout: default
title: Austin Tripp
---
# Austin Tripp
Welcome to [my website](/), thanks for visiting!

I just graduated from [nanotechnology engineering](https://uwaterloo.ca/nanotechnology/) at the 
[University of Waterloo](https://uwaterloo.ca/), and will be starting a PhD at Cambridge in the Fall
in the [machine learning group](http://mlg.eng.cam.ac.uk/?page_id=659).
My primary research interest is how machine learning/AI can be applied to physical sciences,
with particular interest in problems of knowledge incorporation and small datasets.

Click to learn more [about me](/about), see my [CV](/cv),
or read my [blog](/blog) where I [occasionally] write about math, science, language learning,
and my miscellaneous adventures.

## Highlighted blog posts
{% for post in site.categories.frontpage %}
 <li><span>{{ post.date | date_to_string }}</span> &nbsp; <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}



---
layout: default
title: Austin Tripp
---
# Austin Tripp
Welcome to [my website](/), thanks for visiting!

I am currently a 4th year undergraduate student at the [University of Waterloo](https://uwaterloo.ca/),
studying [nanotechnology engineering](https://uwaterloo.ca/nanotechnology/).
My primary research interest is how machine learning/AI can be applied to physical sciences.
My current plan is to pursue graduate studies in machine learning/statistics/applied math in the hope that I can help
bridge the gap between those two understand machine learning and those who understand physical sciences.

Right now I am on a quest to find a supervisor (and a school that will admit me).
If you are a supervisor, or somebody interested in me or my work, feel free to send me an email.
I am open to any/all opportunities.

Click to learn more [about me](/about), see my [CV](/cv),
or read my [blog](/blog) where I write about math, science, and language learning.

## Highlighted blog posts
{% for post in site.categories.frontpage %}
 <li><span>{{ post.date | date_to_string }}</span> &nbsp; <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}



---
layout: default
title: Austin Tripp
---
# Hi there, I'm Austin Tripp
And welcome to my corner of the Internet. I am currently a 3rd year undergrad student at the university of Waterloo. My research interests lie at the intersection of chemical physics and machine learning.I am currently looking to attend graduate school starting in 2019. Feel free to contact me if interested.

*Please note*: I am not interested in doing any wet lab work.

# Highlighted blog posts
\*coming soon\*
{% for post in site.categories.frontpage %}
 <li><span>{{ post.date | date_to_string }}</span> &nbsp; <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}



---
layout: default
title: Austin Tripp's blog
---
# {{ page.title }}
Currently I am using this blog to practice technical writing, organize my thoughts on research papers, and occasionally share something interesting that I find on the internet.

{% for post in site.posts %}
- {{ post.date | date_to_string }}: [{{ post.title }}]({{ post.url }})
{% endfor %}

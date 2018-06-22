---
layout: default
title: Austin Tripp's blog
---
# {{ page.title }}
Note: this is more of a test feature than an actual blog. For the time being I don't intend to update this on a regular basis.

{% for post in site.posts %}
- {{ post.date | date_to_string }}: [{{ post.title }}]({{ post.url }})
{% endfor %}

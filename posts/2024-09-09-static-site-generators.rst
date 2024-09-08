.. title: How I chose a static site generator
.. date: 2024-09-09
.. tags: website
.. category: 
.. type: text

Recently, I wanted to update my website to look a bit more polished (and
support additional features such as automatically generating pages for my
publications). In the end I decided to completely switch from building my
website with Jekyll to `nikola <https://getnikola.com/>`_ instead. This post
explains my thought process for this (in case anybody else is considering
a similar switch).

.. TEASER_END

Main findings
=============

My website is fairly simple, so I only considered static site generators.
When choosing a generator, I considered:

- That my main programming language is python (and I have little knowledge of
  other languages)
- I only needed a basic static website
- I wanted to support a blog, a list of publications, a CV, and a few
  miscellaneous pages

Here are my thoughts on the main static site generators I considered:

Jekyll
------

Pros:

- Simple
- Supported out-of-the-box by GitHub pages
- My website was already in Jekyll
- Lots of nice themes, including a nice `academic <https://academicpages.github.io/>`_ one

Cons:

- Some issues previewing locally: one needed a different version of ruby than
  the default version on Mac, and then needed to install a bunch of "gems".
  I remember this being a pain to set up.
- I don't know the ruby programming language so it's hard for me to interpret
  and modify the features of the website (for example to generate a publication
  page from a bibliography file). I would likely need to look everything up.

Hugo
----

Pros:

- Lots of themes available
- Popular and well-supported
- Good GitHub pages support

Cons:

- I don't know Go so it seemed like it might be hard to do anything custom

Pelican
-------

Pros:

- python-based
- Decent number of themes

Cons:

- A few nice features (like multi-lingual pages and rendering jupyter
  notebooks) were apparently harder to set up than in Nikola

NOTE: my consideration of Pelican was a bit superficial.

Nikola
------

Pros:

- python-based
- Package is very small: not too many hidden features
- There are a few pre-existing add-ons for publications
- Good multi-lingual support
- Decent documentation
- Out-of-the-box support for jupyter notebook pages
- Easy to run locally (just one python package)

Cons:

- Limited selection of templates
- Default is for the site to just be a blog, so making a "website + blog"
  already required a bit of customization
- Templates themselves seem hard to customize

Conclusion
==========

My impression was that all of the static site generators I considered were
pretty good. In the end I chose Nikola. My main reason for this was that the
out-of-the-box website looked decent and had the features I needed. My guess
was that if in the future I needed to do anything fancier, it would be easier
to inspect the package and figure out how to do it than if I used another
framework (especially one that was not python-based). Hopefully my decision is
vindicated in the future.

If you find this list helpful, please do let me know!

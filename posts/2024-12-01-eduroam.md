---
title: "What can eduroam teach us about building research infrastructure"
date: 2024-12-01
tags:
    - speculation
has_math: false
---

Eduroam is a fantastic piece of academic infrastructure: students/researchers
from thousands of universities around the world can _automatically_ connect to
WiFi and any partner institutions using login details from their home
institution. To me it's surprising that it exists, given that it has many
characteristics of projects which academia is _terrible_ at accomplishing:

<!-- TEASER_END -->

- Not academically "interesting" (except possibly for some technical challenges
  at the very beginning)
- Output is not a research paper, instead a piece of infrastructure
- Requires perpetual upkeep/maintenance
- Needs to meet high reliability standards and be fixed quickly

## How did Eduroam get built?

Summarizing [wikipedia](https://en.wikipedia.org/wiki/Eduroam) and a few other
pages, it looks like eduroam started with an idea to connect different national
networks in Europe, and was incrementally adopted by other countries throughout
the 1990s and 2000s. Adoption was relatively easy because:

1. It did not require opting into a centralized login procedure: universities
   could keep their existing independent authentications.
2. Universities already had dedicated IT teams to provide WiFi in their
   buildings (so there was a team in place to handle it).
3. There was already a lot of national infrastructure to connect universities
   within individual countries.
4. Academics (presumably) did not oppose it in any way; in fact it would
   generally make their lives easier.

## What lessons can be drawn for doing large projects in an academic context?

A lot of things which are obvious when you read them:

- Things are easier when infrastructure funding is already available outside of
  the grant system: that removes time limits for project completion and allows
  permanent employees to be hired to maintain it.
- It is easier to link up teams already building similar infrastructure rather
  than building teams from scratch.
- It is best when few (if any) people _oppose_ your project.

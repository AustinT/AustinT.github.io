---
title: "Time zones: why you shouldn't use the terms EST or GMT"
date: 2025-07-13
tags:
    - pedantry
has_math: false
---

This post is about a small mistake in how people discuss time zones which I
find mildly annoying: using the term EST (Eastern Standard Time) to refer to
the current time in cities like New York or Toronto, and GMT (Greenwich Mean
Time) to refer to the current time in the UK. Unfortunately these terms are
_not_ equivalent due to daylight saving time.

<!-- TEASER_END -->

There are only two ways that time zones can work with daylight saving time:
either the time zone itself moves back/forward by 1h, or places change their
time zone. I suppose when time zones were being set up either option could have
been used, but the option used in western countries is the _second_ option, ie
that time zones stay fixed and cities move between time zones. This means that
New York is _not_ in EST in the summer (it is in EDT), and London is not in GMT
(it is in BST).

A more unambiguous way to refer to local times is to just use a city / region /
country name, eg "New York time", "Eastern Time", "UK time".

Why do I find this small thing annoying? Mostly because:

1. If you type a time as written into a computer or digital calendar, you will
   get the wrong time![^calendar]
2. It is a very small change to be correct (eg writing "ET" instead of "EST")

**My ask**: in the US/Canada, you can refer to time zones as PT/MT/CT/ET, not
PST/MST/CST/EST. Refer to time in the UK as simply "UK time" or something
similar.

[^calendar]: Some calendars seem to correct for this but not always, eg "GMT" is a common reference time zone all year and therefore likely won't be autocorrected.

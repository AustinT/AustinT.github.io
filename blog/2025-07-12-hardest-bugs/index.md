---
title: "The hardest bugs are non-bugs"
date: 2025-07-12
tags:
    - programming
has_math: false
---

Debugging computer programs is hard.

<!-- TEASER_END -->

Here I want to share a short piece of hard-earned wisdom which I'm sure has
been written about many times before: _the hardest bugs to fix are non-bugs_,
i.e. instances when you misunderstand what the correct output of your program
should be. Some examples:

- You write a program to add 12+9 and try to figure out why the output is 21
  instead of 22.
- You miscalculate the shortest path in a graph and try to figure out why
  Djisktra's algorithm fails
- You misunderstand the contents of a dataset and try to figure out why the
  summary statistics are wrong.

In these instances, I find that I've spent a lot of time going through a
program line by line only to find that nothing is amiss, and only then do I
figure out that **I** am making the mistake, not the program.

My lesson from this is to try to be really sure of what the expected output of
a program should be before going through it line by line. I'm not always
perfect but I think this attitude has probably saved me a few days of total
time in the past 2 years.

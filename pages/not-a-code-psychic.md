---
title: How to ask for code help effectively (since I'm not a code psychic).
---

# Summary

If I have referred you to this page, then most likely you've asked me for help
with your code without providing enough information for me to help you. Asking
for coding help is a skill itself, and when you are just starting out it might
not be clear what information to provide when asking a question.
Essentially, I think you should provide:

1. A description of the goal of the code _and_ how what you have does not achieve that goal.
2. A _minimal working example_ (MWE).
3. Information about your operating system (e.g. Mac, Windows) and code environment (e.g. python 3.7 with numpy v1.2.3).
4. If helpful, a short description of what you have tried.

These criteria are explained more below, but before diving into that I will give an example of a _good_ request.

## Example of a good request

Hi, I'm trying to compute the logarithm of a number in python, but the program
crashes instead of outputting a number.

I simplified my script down to the following MWE:

```python
import math
print(math.log(0))
```

When I run it, I get the following:

```
Traceback (most recent call last):
  File "~/calculate_log.py", line 2, in <module>
    print(math.log(0))
ValueError: math domain error
```

I am running on MacOS, Python 3.9.16. I Googled this error but cannot find a
clear answer[^1]. Can you suggest what might be going wrong?

[^1]: Note that if you do Google this in real life, you actually do find a clear answer, and I generally expect you to do this level of basic Googling before asking me for help. This is just for illustration purposes.

# Anatomy of a good request 

Here I explain my formula in more detail.

## Description

The essence of code "not working" is that it behaves differently than one
desires. Clearly explaining this divergence is key to framing the issue so that
I know what a "successful" resolution of your problem looks like. This requires
explaining _both_ what your desired outcome is _and_ what you actually observe.

### Part 1: the desired outcome

Sometimes people omit this, thinking that the desired behavior is obvious (and
often it is). But please don't assume this: I may not know the background of
your problem and it is always safer to tell me explicitly what you want.

For example, in the `log(0)` example above the resolution might depend on what you desire:

- If you wanted to compute a logarithm of a general number and put 0 in as a
  placeholder, then the issue is simply that log is not defined at this value.
  Resolution: choose a different placeholder.
- If your goal is to compute `log(0)` specifically, then this goal is
  infeasible, since `log(0)` is not defined. The resolution is that your goal
  does not make sense.

So please, don't leave out this part!

### Part 2: the observed outcome

Generally, "not working" code will either:

1. Crash (and raise an error)
2. Produce an output without crashing, but the output is not what you expect.

It is important to help me understand which of these outcomes it is, because
the steps to resolve them are quite different. Crashing programs have a clear
mistake which need to be identified. Non-crashing programs are usually logic
mistakes (writing the wrong steps by accident) or misunderstanding some
documentation.

If a program crashes, it is helpful to include the error message, because this
almost always contains helpful information. If a program does not crash, then
it is helpful to include its output to save me the time of running it myself.

## Minimal working example (MWE)

A MWE is the simplest way of presenting the error to me. It serves a few functions:

- Saves me the time of writing a program myself to reproduce the error
- Ensures that I can reproduce your error exactly as you see it (instead of
  another version)
- Helps both of us narrow down where the error is occurring

However, not all code is a MWE! Each of the letters (M,W,E) is important. Let's go through them:

### W (working)

Here, "working" does not mean that the code actually works (otherwise you would
not be asking for help). It means that I can 1) run the code and 2) get the
same error as you do.[^2]

[^2]: Perhaps the name "minimal non-working example" would be more apt.

Both parts of this are important:
1. The code should run. This means it must be a complete script, not a code fragment.
2. It should produce the error you observe (not some other error).

For contrast, here is an attempted MWE for the example above which I would not
consider to be "working":

```python
print(math.log(0))
```

Although this is indeed the problematic line of code, when I run it I get a _different_
error because the `import math` statement was not included:

```
Traceback (most recent call last):
  File "~/calculate_log.py", line 1, in <module>
    print(math.log(0))
NameError: name 'math' is not defined
```

Of course, in this simple example I could probably figure out what imports are
missing, but this should not be my job. Please just ensure that it runs.

Importantly, it needs to run for _me_, not just you. For example, if your code
refers to specific files on your computer, then it won't run on my computer
unless I also have those files.

### M (minimal)

The code should be reasonably short (< 100 lines). I probably do not have time
to read through 10000 lines of code (unless you are paying me).

### E (example)

Of course you may fairly ask:

> But Austin, the error is occurring in my 100000 code base. I don't know what
> part is responsible. Shouldn't I include the whole thing?

No! A MWE is, fundamentally, an _example_ of your problem, not a _detailed
record_. When you want to find bugs in a huge code base, you need to find out
what part is responsible, and constructing a small example which reproduces the
problem is an important part of this. Often, the effort of just trying to
construct a MWE will provide the insight needed to solve your problem (without
needing to ask me or be pointed to this document).

## Information on OS and code

This can be brief, but many problems are OS specific, and if I am trying to
debug an issue on a different OS than you I should at least know that. Also,
knowing the version of python and versions of your python library can help
(again, because some issues will only appear on certain versions).

## Description of what you have tried

Already, the act of creating a MWE was probably enough. If however you spent
time researching possible causes for the issue, it could be helpful to tell me
(since it may save my time later on).

# Common mistakes

Here are some unhelpful patterns which I would like to highlight in particular:

## "Not working" as a description

> Hi, my code below is not working, can you help?

I need to know more specifically what you consider to be "working" and what is
actually happening. Read above.

## No MWE

> I'm trying to compute the logarithm of small positive numbers but am getting
> a "math domain error" even though they are in the domain of the log function.
> Can you help?

How small are the numbers? What programming language are you using? What
logarithm implementation? I do not know these things and therefore cannot be of
much help. This is where a MWE is helpful.

## Screenshots

Please do not screenshot error messages you get: include them as text. This
helps me Google them without needing to re-type them. It's only marginally
slower for you, but much faster for me.

## Custom files/packages

If your MWE looks like:

```python
import my_custom_package
f = open("file/on/my/computer.txt")
my_custom_package.process_file(f)
```

then I probably cannot run it unless I have access to the same package and same
files on your computer. Please ensure that I can also run the MWE.

## GPUs/CUDA

If your code uses `pytorch` or similar, it is relevant to know whether your
machine has a GPU and if so, what version of CUDA it is running. Please include
this. A lot of errors end up being GPU-specific.

# Why this webpage?

Enough people have asked me for code help without providing enough information
that I thought it would be easier to write a good answer once and link to it
instead of writing a bespoke answer every time. Also, in the past I have found
it hard to resist putting in some sarcastic comments along the line of "I'm not
a code psychic" which were probably not helpful 😅

# Further reading

I also found this guide from [Stack Overflow](https://stackoverflow.com/help/how-to-ask) helpful.

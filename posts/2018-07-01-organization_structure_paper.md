---
title: "Paper Review: A Computational Approach to Organizational Structure"
date: 2018-07-01
categories:
    - Papers
    - frontpage
mathjax: true
---

## Motivation
Ever since I've started doing internships, the concept of efficient organizations has piqued my interest. In every workplace I have been in, time is always wasted by inefficient transfers of information. For example, long meetings where most of the content is irrelevant to most of the people, or repeated interactions with co-workers where you explain the same thing to all of them. Assuming employees make ~$40/hour, a 1 h meeting with 100 people will cost $4000! If these meetings are not productive, then the company gets a negative return on its time investment, which essentially means the company is wasting money. Clearly organizational efficiency is a financially important objective.

Much of an organization's efficiency can be linked to its structure. Long, big meetings are usually a consequence of a strong _hierarchical_ organization, where work is done by employees, then synced to a centralized node (a boss), and then possibly recapitulated to the workers in a meeting. However, are there better ways to structure an organization that would save time?

## The Paper
The paper [A Computational Approach to Organizational Structure](https://arxiv.org/abs/1806.05701) tries to address this problem from a fundamental perspective. They frame the problem as such:
- Model an organization as a _graph_ with the nodes being people, and the edges being connections between them. For example, a hierarchical organization would be a tree
- Model tasks as _tokens_, where each node (person) has tokens which they can do the following with:
  - _Compute_ with two tokens, to form one token
  - _Transmit_ one token to a neighbouring node
 These actions are assumed to take $$t_c$$ and $$t_m$$ respectively.

As a sample problem, the paper chooses to analyze the _information aggregation_ problem, which means taking all the tokens (tasks) and combining them at one node. This is equivalent to passing around information: for example, doing an analysis of which items to purchase for the company, then condensing and passing the recommendations to the CEO to make the final decision.

## Their algorithm
The paper presents 2 things:
- An exact, polynomial time algorithm for solving the problem on fully-connected graphs
- An approximate algorithm for solving it on arbitrary graphs.

The exact algorithm is essentially a hierarchical approach: given a tree, the leaf nodes pass their tokens to their parents, who compute it, and pass the tokens to their parents, etc. They give a formula for designing the optimal tree recursively. To make this work on an arbitrary graph, simply embed the tree in the graph. I talk about this algorithm in more detail [below](#more-detailed-explanation-of-the-fully-connected-graph-optimization).

The approximate algorithm is similar in intuition. Designate some nodes as sources, and the rest as sinks. Then pass tokens from sources to sinks, which then aggregate the tokens together.

The bulk of the paper is essentially dense math proving that these solutions run in polynomial time. 

## My thoughts on the paper
I won't lie: I didn't read the proofs for this. But the intuition was very interesting. Essentially the result of the paper supported a hierarchical information transfer process, at least for centralized transfer of information. I think it would be interesting to consider the downwards transfer of information too, or modelling a multi-step decision process with feedback.

Another analogous problem that I think is interesting not only propagating information to a central source, but as work gets done, propagating information on that work to all other nodes (i.e. keep people up to date on what other people are doing). This is another problem I have observed in big companies. The analogous idea here would probably be each computation generating its own mini-token, which should be processed and passed around to all other nodes in the network (in some form).  


## More detailed explanation of the fully-connected graph optimization
I found this quite interesting, so I thought I would elaborate more on it. The key formula is defining a tree $$T(R)$$ as the largest tree such that information can be greedily aggregated within R time steps. The formula for such a tree is:

$$T(R) = \begin{cases}
\text{Single leaf},  & \text{if $R < t_m < t_c$} \\
T(R-t_c) \text{ with child } T(R-t_c-t_m), & \text{otherwise}
\end{cases}$$ 

This can be interpreted in a simple way: if a node  has a child, then it will take $$t_m$$ time to get the token from the child node, and $$t_c$$ to compute it. So if $$R < t_m + t_c$$, then there is no way to complete the computation in $$R$$ rounds. So the tree cannot have any leaves.

Otherwise, the tree can have leaves. So the largest tree you can create is the largest tree you can make and still have enough rounds left for one computation ($$T(R-t_c)$$), with an additional leaf tree which can be fully computed, and still have time to pass its message to the root ($$T(R-t_c-t_m)$$).

I really liked this formula because it was so clean and recursive.


---
title: "Turning Adam Optimization into SGD"
categories:
    - MachineLearning
    - frontpage
layout: post
mathjax: true
---

## Motivation
This strange question came up when working on a machine learning project to generate embeddings. 
Working with the version of Pytorch available on our DGX (similar to version 0.3.1), I found there was an optimizer called _SparseAdam_ but not one called _SparseSGD_.
Since what I really wanted to do was use SGD, I wondered: could I turn the Adam optimizer into an SGD optimizer by setting the hyperparameters $$\beta_1$$, $$\beta_2$$, and $$\epsilon$$?

## The Answer
Probably not. Looking at the [original paper for Adam](https://arxiv.org/abs/1412.6980), the formula for the parameter updates is:

$$\theta_{t+1} = \theta_t - \alpha * \frac{\hat{m}}{\sqrt{\hat{v}_t}+\epsilon}$$

To make this equal to gradient descent, we need the second term to equal the gradient.

Luckily, $$m_t$$ is directly related to the gradient, via the equation:

$$m_t = \beta_1 m_{t-1} + ( 1- \beta_1) \nabla \theta_t$$

$$\hat{m_t} = \frac{m_t}{1-\beta_1^t}$$

 Clearly, setting $$\beta_1=0$$ will set the value to the gradient value. Note that this will also mean the normalization doesn't change $$m_t$$.

The problem is the term $$\hat{v}_t$$, defined as:

$$v_t = \beta_2 * v_{t-1} + (1-\beta_2) (\nabla \theta_t)^2$$

$$\hat{v_t} = \frac{v_t}{1-\beta_2^t}$$

We want this term to equal 1, to disappear from the fraction. However, setting $$\beta_2=0$$ will cause it to be proportional to the square of the gradient, and setting $$\beta_2 = 1$$ will cause a division by 0 error in the normalization. So because of this, I don't see a way to convert Adam into SGD. The gradient normalization is just build in too much into the algorithm.  

## Conclusion
I don't think it is possible. And after reading the docs again, SGD is already compatible with sparse matrices, so this was completely unnecessary. It was a fun thought exercise though.

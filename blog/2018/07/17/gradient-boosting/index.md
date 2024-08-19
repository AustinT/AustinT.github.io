---
title: "An Overview of Gradient Boosting and Popular Libraries for it."
date: 2018-07-17
categories:
    - MachineLearning
    - frontpage
mathjax: true
---

Everybody doing machine learning wants the best models possible. 
The aim of this blog article is the following:

1. To provide an introduction to the machine learning technique known as _boosting_, and specifically _gradient boosting_.
2. To compare/contrast boosting with other ensemble methods, such as _bagging_
3. To explain and compare several popular gradient boosting frameworks, specifically _XGBoost_, _CatBoost_, and _LightGBM_.

## A brief introduction to ensemble models
Machine learning tasks can be framed as a function approximation task, where the goal is to approximate a function \\(f(\vec{x})\\) given a set of observations 
\\(\lbrace \left(\vec x_i, f(\vec x_i) \right)\rbrace _{i=1:N}\\).
The main difficulty is that \\(f\\) can be very complex, or potentially we might not have a lot of data. So a simple model (e.g. linear regression) might not be able to adequately model \\(f\\), and a sufficiently complex model would overfit the training set.

This kind of scenario is perfect for an ensemble method: where multiple models are combined together to create one superior model. Two popular methods for this are called _bagging_ and _boosting_.

### Bagging
Personally, I find this method to be more intuitive. The intuition behind bagging is that different models tend to make different kinds of errors, so given many models, it is unlikely that they will all make a similar misclassification error. Therefore, you train multiple models, and to inference on a data point you inference on all the models and then average/vote on the result.

However, how do you guarantee that all the models will make different kinds of errors? Most simple models are fit using deterministic algorithms, meaning that training multiple copies of the same model won't yield any different results. The answer for this is _bootstrapping_, which is the statistical name for subsampling from your data. By training models on different subsets of your training set, each point is only seen by a fraction of the models, and therefore not all the models will be able to overfit to that point. Furthermore, since the different models will also all see different data _distributions_, they will also be unable to precisely overfit to your training set distribution. The overall effect of this is that the different models you train will be significantly less correlated, making the above objective of independent errors more true.

This technique is what gives _bagging_ its name: it stands for _"Bootstrap AGGregatING"_. (I used to think it was called bagging because you had a "bag of models", but this is not the case).

Moving up one level of abstraction, bagging can be thought of as a weighted averaging model: given the outputs of several models, the bagging model assigns a weight to each of the model's predictions and sums them to get a total prediction. Assuming the bagging method uses N models, an averaging bagging model assigns a weight of \\(1/N\\) to each sub-model, and a mode bagging model assigns a weight of \\(1/N_{mode}\\). 

### Boosting
Boosting differs from bagging in the fitting procedure, and in the goal of each model. In bagging, the goal is to train models independently so that they make less correlated errors. In boosting however, models are trained sequentially, with the goal of training each model being to correct for the errors made by the previous model.

That is, if you have a model \\(m_j(\vec{x})\\) fit after \\(j\\) iterations, then the goal of boosting is to fit a model

$$m_{j+1}(\vec{x}) = f(\vec{x}) - m_j(\vec{x})$$ 

This essentially means that you are fitting a new model, such that when it is added to the previous model, perfectly corrects for its mistakes. Intuitively, you are training a model that _boosts_ the performance of your previous model, hence the name boosting.

## Gradient boosting
_Gradient boosting_ is a specific variety of boosting, with a slightly different objective. Consider the following scenario: you would like to fit your entire dataset, but there is a specific region which you care more about, so errors in that region are more problematic than errors in other regions. One example of this kind of scenario would be medical diagnosis, where a false negative (saying no disease when there is really a disease) can have severe consequences. In this case, trying to match every point equally would not be the best choice.

Typically in this kind of scenario, a _loss function_ is used to capture the error preferences in a single scalar value. In this context, the goal of adding another model to your set of models is not to decrease the fitting errors, but to decrease the loss function. Specifically, you would like it so that:

$$L(m_{j+1} + m_j) \leq L(m_{j+1})$$

One way to do this is to make \\(m_{j+1}\\) proportional to the loss gradient. By making \\(m_{j+1} = \nabla_{m_j} L(m_j)\\), we know that adding (subtracting) \\(m_{j+1}\\) will cause an increase (decrease) in the loss function, because the gradient gives the direction of steepest increase.

However, because the gradient might vary significantly within a short distance, we multiply the gradient by a small constant to improve the accuracy of this first order approximation. 

So in summary, the difference between gradient boosting and normal boosting is the objective function. In normal boosting, we want:

$$m_{j+1}(\vec{x}) = f(\vec{x}) - m_j(\vec{x})$$

Whereas in gradient boosting, we want:

$$m_{j+1} = \nabla _{m_j} L(m_j)$$

Note that like bagging, since the outputs of different trees are being added to produce the final output, it can also be thought of as a weighted averaging model.

## Gradient boosting and decision trees
Usually when gradient boosting is discussed, it is almost always in relation to decision trees. Why is that? While I am not 100% sure of this, I can think of a few main reasons:

- With linear models (i.e. linear regression), the models are already additive, so adding two linear models is always equivalent to fitting a single linear model
- The gradient might be very high for a few training examples, and low for the rest (e.g. if only a few examples are misclassified). With most models, changing the parameters will affect all of the results, whereas with decision trees you can simply add a new leaf node to an existing leaf to further fit those specific examples, allowing you to increase accuracy for those examples while not sacrificing it for other examples.
- There are nice analytic updates about whether to split a node in a decision tree, while for other models (e.g. neural nets) the fitting takes a long time.
- Newer models (neural nets) are usually pretty strong learners, and in theory if the neural network consistently performs poorly on a specific output you can just train on that output more, or add more parameters to increase model complexity. So gradient boosting doesn't seem very necessary for this.

So while it seems like gradient boosting can be used for anything, in practice it is mainly used for decision tree models.

## High-level comparison of gradient boosting frameworks
_XGBoost_, _CatBoost_, and _LightGBM_ are all popular gradient boosting frameworks for decision trees. They all use essentially the same algorithm for one part of it, with the difference being in the other part. The two steps for most gradient boosting algorithms are:
1. An algorithm to produce candidate new trees, usually iteratively, by given a starting tree, by selecting a leaf node to split and performing a split. Usually the first tree in this algorithm is just a single leaf node (i.e. all items in one node)
2. An algorithm to evaluate the quality of these splits.

The common part is usually #2, the evaluation algorithm, since this is usually just the loss reduction caused by the split. The frameworks mainly differ in how they reduce the computationally hard problem of producing candidate trees. Roughly speaking, these are how the above 3 algorithms work:

- *XGBoost*: Given an existing tree, the naive way to improve it would be to iterate over every possible split value for every possible feature, and calculate the loss for each split, then choose the best split. Note that iterating over every possible split realistically just means iterating over every feature value for every data point, since the only goal is partitioning your set of training data, meaning that two splits that yield different partitions are not useful.  
 XGBoost notes that this iteration isn't efficient for large datasets, so they portion the dataset into quantiles for each feature, and do their partitions based on the quantiles. This results in a more efficient, but still slightly brute force method.
 [This is the link to the XGBoost paper that explains it in more detail](https://arxiv.org/abs/1603.02754) 
- *CatBoost*: one of the main ideas behind CatBoost is that if a data point is used to produce a model, then boosting it using the same data gives a biased estimate of the gradient (biased with respect to the underlying data distribution). They counteract this by training an ensemble of models based on different permutations of the data, where each model is boosted using only new data points (i.e. data points it hasn't seen before). The multiple permutations ensure that each data point has the chance to be used for a _good_ model, since the first few points in a given permutation are going to be used to boost models trained on _even fewer points_, so the model will be bad.  
 In addition, CatBoost also has some unique ways of handling categorical variables. [This is the CatBoost paper, which provides more detail](https://arxiv.org/abs/1706.09516)
- *LightGBM*: Microsoft's LightGBM does 2 things. Firstly, they throw away data points which have small gradients, reducing the amount of data that they have to calculate splits over (this is done heuristically). Secondly, they bundle features which are mutually exclusive, effectively taking two features X and Y and doing computations with a new feature, (X or Y). This is also estimated heuristically. [See the original paper for more details](https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree)

So in summary, the main difference between these libraries is how they choose to reduce the number of splits that they investigate, and which points they choose to make/evaluate those splits. But the underlying split evaluation idea is almost identical.

## Conclusion
In summary, I've explained what bagging and boosting are, and some of the key gradient boosting libraries. Even though boosting techniques don't seem very prominent in modern machine learning literature, I think they are still valuable to know. They are especially useful for serving machine learning models at scale, where simple models like decision trees have huge speed advantages on large datasets. So I believe that boosting/gradient boosting will prove useful well into the future.

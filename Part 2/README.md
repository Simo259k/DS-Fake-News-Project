# Part 2 - Simple Logistic Regression Model (~1 page)
You should create one or more reasonable baselines for your Fake News predictor. These should be simple models that you can use to benchmark your more advanced models against. You should aim to train a binary classification model that can predict whether an article is reliable or fake.

## Task 0
Briefly discuss how you grouped the labels into two groups. Are there any limitations that could arise from the decisions you made when grouping the labels?

## Task 1 
Start by implementing and training a simple logistic regression classifier using a fixed vocabulary of the 10,000 most frequent words extracted from the content field, as the input features. You do not need to apply TF-IDF weighting to the features. It should take no more than five minutes to fit this model on a modern laptop, and you should expect to achieve an F1 score of ~94% on your test split. Write in your report the performance that you achieve with your implementation of this model, and remember to report any hyper-parameters used for the training process.

## Task 2 
Consider whether it would make sense to include meta-data features as well. If so, which ones, and why? If relevant, report the performance when including these additional features and compare it to the first baselines. Discuss whether these results match your expectations.

## Task 3 
Apply your data preprocessing pipeline to the extra reliable data you scraped during Graded Exercise 2 and add this to the training data and observe how this changes the performance of your simple model. Discuss whether you will continue to use this extra reliable data for the Advanced Model.

For the remainder of the project, we will limit ourselves to main-text data only (i.e. no meta-data). This makes it easier to do the cross-domain experiment in Part 4 (which does not have the same set of meta-data fields).

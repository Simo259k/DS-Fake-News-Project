# Part 3 - Advanced Model (~1 page)

## Create the best Fake News predictor that you can come up with. 
This should be a more complex model than the simple logistic regression model, either in the sense that it uses a more advanced method, or because it uses a more elaborate set of features. For example, you might consider using:
1. Support Vector Machine
2. Naive Bayes Classifier
3. Neural network.
The input features might use more complex text representations, such as TF-IDF weights or continuous word embeddings.

## Report necessary details about your models ensuring full reproducibility
This could include, for example: 
1. The choice of relevant parameters and how you chose them.
Make sure to argue for why you chose this approach over potential alternatives.

## Optional 
If you want to go even further, you might want to try training your models on even more data. The full FakeNewsCorpusLinks to an external site. is a total of 9GB of source material available for training your model. You will need to use a multi-part decompression tool, e.g. 7z. Given all the files, execute the following command: 7z x news.csv.zip. This should create a 27GB file on disk (29.322.513.705 bytes). You may find it challenging to run your data processing pipeline on the entire FakeNewsCorpus, so take care if you attempt this step.

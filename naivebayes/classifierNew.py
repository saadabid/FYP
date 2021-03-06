# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:27:46 2017

@author: Muhammad Saad
"""

import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
# calculate accuracy
from sklearn import metrics
import numpy as np
dataSet = pd.read_csv("intentsfilenewedit.csv", names=["inputs", "intents"])
len(dataSet)
def text_process(mess):
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text
    """
    nopunc = [char for char in mess if char not in string.punctuation]

    nopunc = ''.join(nopunc)
    
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),  # strings to token integer counts
    ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
    ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
])

msg_train, msg_test, label_train, label_test = \
train_test_split(dataSet['inputs'], dataSet['intents'], test_size=0.3)

print(len(msg_train), len(msg_test), len(msg_train) + len(msg_test))

with open('conversationpre2.pickle','wb') as f:
    pickle.dump(pipeline.fit(msg_train,label_train),f)

print("Classification Report for Naive Bayes")
print("---------------------------------------------------")    
predictions = pipeline.predict(msg_test)
print(classification_report(predictions,label_test))
accuracy = metrics.accuracy_score(label_test, predictions)
print("  Accuracy : ",accuracy*100)
print("---------------------------------------------------")

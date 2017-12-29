# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 22:05:00 2017

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
import numpy as np

dataSet = pd.read_csv("intentsfilenewnew.csv", names=["inputs", "intents"])
len(dataSet)

def text_process(mess):
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text
    """
    # Check characters to see if they are in punctuation
    nopunc = [char for char in mess if char not in string.punctuation]

    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    
    # Now just remove any stopwords
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),  # strings to token integer counts
    ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
    ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
])
pipeline.fit(dataSet["inputs"],dataSet["intents"])

#predictions = pipeline.predict(["How is the it's likely to rain today"])
#print(predictions)

pickle_out = open("classifier.pickle", "wb")
pickle.dump(pipeline, pickle_out)
pickle_out.close()

pickle_in = open("classifier.pickle", "rb")
myclassifier = pickle.load(pickle_in)

clpredictions = myclassifier.predict(["price delivery charges"])
print(clpredictions)

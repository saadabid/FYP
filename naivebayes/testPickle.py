# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 22:31:00 2017

@author: Muhammad Saad
"""

#import nltk
import string
from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize
import pandas as pd
import pickle
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.feature_extraction.text import TfidfTransformer
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.metrics import classification_report
#from sklearn.model_selection import train_test_split
#from sklearn.pipeline import Pipeline
import numpy as np
import sys


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

pickle_in = open("svmPredictions.pickle", "rb")
myclassifier = pickle.load(pickle_in)

#lines = sys.stdin.readlines()

clpredictions = myclassifier.predict(["How I pay ?"])
#print(clpredictions)

awnser = pd.read_csv("awnser.csv", names=["Delivery Time", "Delivery Charges","Delivery Method","Payment Method","Order","Order Status","Discount","Price"])
#print(awnser)

if (clpredictions== "Delivery Time"):
   reply = awnser['Delivery Time'][0];
elif (clpredictions== "Delivery Charges"):
   reply = awnser["Delivery Charges"][0];
elif (clpredictions== "Delivery Method"):
   reply = awnser["Delivery Method"][0];
elif (clpredictions== "Delivery Charges"):
   reply = awnser["Delivery Charges"][0];
elif (clpredictions== "Payment Method"):
   reply = awnser["Payment Method"][0];
elif (clpredictions== "Order"):
   reply = awnser["Order"][0];
elif (clpredictions== "Order Status"):
   reply = awnser["Order Status"][0];
elif (clpredictions== "Discount"):
   reply = awnser["Discount"][0];
elif (clpredictions== "Price"):
   reply = awnser["Price"][0];
else:
   reply = "Our representative will respond you soon."

replystr = clpredictions.tostring;
#replywrite = reply , "|" , replystr)
print(reply , "|" , clpredictions)
"""Filename: hello-world.py
  """

from flask import Flask
import os
#import textprocess
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
#import numpy as np
import sys


#pickle_in = open("classifier1.pickle", "rb")
#myclassifier = pickle.load(pickle_in)

#clpredictions = "workrd but not"
#clpredictions = myclassifier.predict(["price"])
#print(clpredictions)

#processed = text_process("hello world")
#print(processed)

#pickle_out = open("dict.pickle", "wb")
#pickle.dump(processed, pickle_out)
#pickle_out.close()

#pickle_in = open("dict.pickle", "rb")
#e_d = pickle.load(pickle_in)
#print(e_d)

#print("helloxzyz")

#execfile('testPickle.py')
#exec(open('testPickle.py').read())

#os.system('python testPickle.py')
#resDF = pd.read_csv("response.csv", names=["response"])
#print(resDF["response"])

#f = open('helloworld.txt','r')
#message = f.read()
#print(message)
#f.close()

app = Flask(__name__)

@app.route('/users/<string:username>')

#import textprocess

def hello_world(username=None):
	print(username)
	username = username.replace('-', ' ')
	print(username)
	f = open('question.txt', 'w')
	f.write(username)
	f.close()
	os.system('python testPickle.py')
	f = open('helloworld.txt','r')
	message = f.read()
	print(message)
	f.close()
	#message = "abc"
	return(message + "| {}!".format(username))

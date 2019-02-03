# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 00:33:23 2018

@author: Srinjoy Santra
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('training_set.csv')
datasete = pd.read_csv('test_set.csv')  

# Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def bag_of_words(ds,length):
    corpus = []
    
    for i in range(0, length):
        topic = re.sub('[^a-zA-Z]', ' ', ds['Topic'][i])
        topic = topic.lower()
        topic = topic.split()
        ps = PorterStemmer()
        topic = [ps.stem(word) for word in topic if not word in set(stopwords.words('english'))]
        topic = ' '.join(topic)
        corpus.append(topic)
    return corpus
    
# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 200)
length=len(dataset.index)
corpus = bag_of_words(dataset,length)
X_train = cv.fit_transform(corpus).toarray()
length=len(datasete.index)
corpus = bag_of_words(datasete,length)
X_test = cv.fit_transform(corpus).toarray()

headers = list(datasete)
df=pd.DataFrame({'Topic':datasete['Topic']})
#cm=np.array([[0,0],[0,0]])
from sklearn.metrics import confusion_matrix
for j in range(2,9):
    y_train = dataset.iloc[:, j].values

# Splitting the dataset into the Training set and Test set
#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.37,shuffle=False)

    # Fitting Naive Bayes to the Training set
    from sklearn.naive_bayes import GaussianNB
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)
    
    # Predicting the Test set results
    y_pred = classifier.predict(X_test)
    dff=pd.DataFrame({headers[j]:y_pred})
    df=df.join(dff)
    
    
    #cm = cm + confusion_matrix(y_train, y_pred)

df.to_csv('predicted.csv', sep=',',columns=headers)

    
    

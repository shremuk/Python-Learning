# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 17:37:42 2018

@author: DELL
"""

import pandas as pd
import numpy as np
import math
import operator
import os
import sklearn

os.chdir("D:\Data Science\Iris")
data = pd.read_csv("iris.csv")
data.rename(columns = {'SepalLength':'sepal-length', 'SepalWidth':'sepal-width', 'PetalLength':'petal-length', 'PetalWidth':'petal-width', 'Name':'Class'})
data.isnull().any()
X = data.iloc[:, :-1].values  
y = data.iloc[:, 4].values 

# Spliting into train and test data
from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 20) 

# RandomState = 

from sklearn.preprocessing import StandardScaler  
scaler = StandardScaler()  # It's like a mould 
scaler.fit(X_train)    # This function will understand the mean and std dev of each column

X_train = scaler.transform(X_train)  # this will tranform the data UNTIL mean = 0 and stddev = 1
X_test = scaler.transform(X_test)  

from sklearn.neighbors import KNeighborsClassifier  
classifier = KNeighborsClassifier(n_neighbors=5)  # classifier fits data into distances
classifier.fit(X_train, y_train)  # measures distance b/w x and y train points

from sklearn.neighbors import KNeighborsClassifier  
classifier = KNeighborsClassifier(n_neighbors=5)  # trying to understand weights
classifier.fit(X_train, y_train)  # Calculate w1, w2 = sq.rt(w1 * distance b/w x2-x1)
y_pred = classifier.predict(X_test)  # Using weights calculated during train, now we are applying it on test data to predict results, y_pred is saving the results

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score 
print(confusion_matrix(y_test, y_pred))  
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))




























# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 23:41:32 2019

@author: DELL
"""

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from numpy import nan as NA
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import seaborn as sns
import os
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')


os.chdir("D:\Data Science\Capillary dataset")
data = pd.read_csv("product_attributes.csv")
data.head()
data2 = pd.read_csv("train.csv")    # Once we put the folder path, neednot mention it again
data2.head()
data2 = data2.merge(data, on = 'productid', how = 'left')
data2.head()


#Finding no. of unique products

data2['productid'].unique()
data2['productid'].count()


#Monthly wise top products

data2['OrderDate'] = pd.to_datetime(data2['OrderDate'], format="%d-%m-%Y")
data2['OrderDate'].head()


# Top 10 products sold


data2['productid_bins'] = pd.cut(data2['productid'], bins = 50)
data2.head()
data3 = pd.crosstab(data2.productid_bins, data2.Quantity)
data3.head()
data3 = data3.reset_index()
data3.head()


# Monthly 































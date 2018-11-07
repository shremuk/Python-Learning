# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 20:20:18 2018

@author: DELL
"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
obj = pd.Series([4, 7, -5, 3])
obj
obj.values
obj.index

#identifying values through given index
obj2 = pd.Series([4, -5, 6, 7], index = ['d', 'b', 'a', 'c'])
obj2
obj2.index
obj2[2]
obj[1:3]
obj[2:]
obj2[:3]
obj2[obj2>0]
obj2 * 2
np.exp(obj2)
obj2[['d', 'a']]

# Creating a series from Dict
sdict = {"Ohio": 35000, "Chicago": 71000, "NY": 42000, "Dallas": 53000}
ser = pd.Series(sdict)
ser
states  = ["Ohio", "Chicago", "NY", "Dallas"]
#Displaying indexes in the same format as given in dictonary
obj3 = pd.Series(sdict, index = states)
obj3

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

data = {'States': ['Ohio', 'Nevada', 'Love', 'Dalas', 'Nevada'],'Year' : ['2000','2002','2004','2005','2006'],'Values': ['1.1','1.3','1.3','1.5','1.8']}
frame = pd.DataFrame(data)
frame
frame.head()
frame2 = pd.DataFrame(data, columns = ['Year','States','Values','House'], index = ['a','b','c','d','e'])
frame2
frame2.Year
frame2['States']
frame2.loc["c"]
frame2['House'] = 16.5
frame2
frame2['House'] = ['Ok','Pk','Ck','Dk','Fk']
frame2
frame2['House'] = np.arange(5.)
frame2

val = pd.Series(['-1.2','-1.666','-1.256'], index =['b','d','e'])
frame2["House"] = val
frame2
frame2['eastern'] = frame2.States == "Ohio" # getting true values for all states input
frame2
frame2.values
del

pop = {'Nevada': {2001: 2.4, 2002: 2.9},'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
frame3
frame3.index.name = 'Year'; frame3.columns.name = 'State'
frame3.T


# Index Objects




import pandas as pd
from pandas import Series, DataFrame
import numpy as np

obj = pd.Series([3, -6.5, 7, 8], index = [ 'd','b','c','a'])
obj
obj2 = obj.reindex(['a','b','c','d','e'])
obj2 #error
obj3 = pd.Series(['blue', 'purple', 'yellow'], index = [0,2,4])
obj3
obj3.reindex(range(6), method = 'ffill')  #error
obj3

frame = pd.DataFrame(np.arange(9).reshape(3,3), index = ['A','C','D'], columns = ['Ohio', 'Texas','California'])
frame
frame.reindex(['A','B','C','D'])
states = ['Ohio', 'Texas', 'Utah', 'California']
frame.reindex(columns=states)
frame.loc[['A','B','C','D'], states] #displaying reindexed column and row

# dropping a value

ass = pd.DataFrame(np.arange(6.), index = ['a','b','c','d','e','f'])
ass
ass.drop('c')
ass.drop(['d','e'])

yourass = pd.DataFrame(np.arange(16).reshape(4,4), index = ['Rough','Smooth','Silk','Hard'], columns = ['Ck','Dk','Nk','Pk'])
yourass
yourass.drop(['Rough','Hard'])
yourass.drop(['Dk','Nk'], axis = 1)

# indexing

obj = pd.Series(np.arange(9), index = ['a','b','c','d','e','f','g','h','i'])
obj
obj['c']
obj['c':'f']
obj[obj<7]
obj[3:5] = 345
obj


yourass = pd.DataFrame(np.arange(16).reshape(4,4), index = ['Rough','Smooth','Silk','Hard'], columns = ['Ck','Dk','Nk','Pk'])
yourass
yourass['Dk']
yourass[['Dk','Nk']]
yourass[:3]
yourass[:1]
yourass < 5
yourass[yourass < 5] = 0
yourass

yourass.loc['Rough', ['Dk','Pk']]
yourass.iloc[2,[3,0,1]]
yourass.iloc[[1,2],[3,0,1]]
yourass.loc[:'Silk', ['Ck','Dk']]
yourass.iloc[:,:3][yourass.Dk>9]

# Arithmetic operations

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
s1
s2
s1+s2

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df1
df2
df1+df2
1/df1
1/df2


import pandas as pd
from pandas import Series, DataFrame
import numpy as np

df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})
df1
df2
df1+df2

#Arithmetic methods with fill values

pd1 = pd.DataFrame(np.arange(12.).reshape((3,4)), columns = list('abcd'))
pd2 = pd.DataFrame(np.arange(20.).reshape((4,5)), columns = list('abcde'))
pd1
pd2
pd1+pd2
pd1.add(pd2, fill_value = 0)

# Arithmetic Operations b/w Series and DF

arr = np.arange(4).reshape(2,2)
arr
arr - arr[1]

df = pd.DataFrame(np.arange(12.).reshape((4,3)), columns = list('bde'), index = ['Ohio','Ontario', 'Canada', 'Tokyo'])
df
df.iloc[1]
df-df.iloc[1]

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
frame
np.abs(frame)
# functins using DataFrames
f= lambda x: x.max() - x.min()
frame.apply(f)

obj = pd.Series(np.arange(5), index = ['e','a','d','b','c'])
obj
obj.sort_index()
obj = pd.Series([4, 7, -1234, 45])
obj
obj.sort_values(ascending = False)

frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
frame
frame.sort_values(by = 'b')
frame.sort_values(by = ['a','b'])

avg = np.arange(10)
avg
avg.mean()

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

obj = pd.Series(np.arange(10), index = ['a','a','b','d','c','d','f','f','e','g'])
obj
obj.index.is_unique
obj['a']
obj['d']
obj[['d','b']]

obj2= pd.DataFrame(np.random.randn(4,3), index = ['a','a','b','b'])
obj2
obj2.loc['b']

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
df
df.sum()
df.sum(axis = 'columns')
df.cumsum()

obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
obj
uniques = obj.unique()
uniques
obj.value_counts()

# Histogram

data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4], 'Qu2': [2, 3, 1, 2, 3], 'Qu3': [1, 5, 2, 4, 4]})
data
result = data.apply(pd.value_counts).fillna(0)
result

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

type examples/ex1.csv
a,b,c,d,message
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo

import os
os.chdir("C:\\Users\\DELL\\Desktop\\bank")

data = pd.read_csv('bank.csv', sep =';')
data.describe()

data.corr()
data.cov()

data.dtypes
data.to_csv('bank2.csv') 
data













































































































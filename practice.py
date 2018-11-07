# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:57:51 2018

@author: DELL
"""

list1 = {"25":"Square root of 5", "Pi": "3.14", "ME": "What's your name"}
list1.keys()
list1.values()
print("The value corresponding to " + str("25") + " is: " + list1["25"])
emptyvar = {}
emptyvar[25] = "Square of negative 5"
print(emptyvar)

tup = (2, 4, 6), (3, 5)
tup
nested_tup = (4, 5, 6), (7, 8)
nested_tup
tuple([4, 0, 2])
tup = tuple('string')
tup
tup[2]
tup = tuple(['foo', [1, 2], True])
tup[1]
tup[1].append(3)
tup[1]
x = (4, None, 'foo') + (6, 0) + ('bar')
x
x[2]

tupl = (4, 5, 6)
(l, m, n) = tupl  
n

#swapping
a, b = 2, 3
a, b = b, a
b

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
seq[1]

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print('a={0}, b={1}, c={2}'.format(a, b, c))

values = 1, 2, 3, 4, 5
a, b, *rest = values
a, b
rest

a = (1, 2, 2, 3, 4, 5, 6, 6, 6, 7, 7 , 8 , 9)
a.count(7)


a = (1, 3, 5, "rest")
"rest" in a
b = list(a)
print(b)
b.append(45)
b
type(b)
type(a)

f = range(0,30)
list(f)


sun = [23456, "append", "love"]
sun.extend([789, 234,(96, 45)])
sun

a = [67, 98, 4, 6, 1, 9]
a.sort()
a

b = ['saw', 'small', 'He', 'foxes', 'six']
b.sort(key=len)
b

seq = [7, 2, 3, 7, 5, 6, 0, 1]
seq[1:4] #slicing
seq[1:4]= [4, 5, 6]
seq  #overwriting slicing

yar= [1, 0, 6, 5, 3, 6, 3, 2, 7]
seq[::-1]
seq


i = 0
for value in collection:
# do something with value
    i += 1
i


some_list = ['foo', 'bar', 'baz']
mapping = {}
for i, v in enumerate(some_list):
    mapping[v] = i
mapping


sorted("prudhvi potuganti")

set([2, 2, 2, 1, 3, 3])


p = {1, 3, 4, 8, 9, 23}
q = {1, 4, 7, 9, 33}
p.union(q)
p | q
p.intersection(q)
p & q


words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}

for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)

by_letter


all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
e_count = [name for names in all_data for name in names if name.count("e") >= 2]
e_count

#while loop
b = 1
while b <= 10:
    print(b)
    b+=2

c = 0
while c <= 10:
    print(c)
    c+=2

age = int(input("Enter your age"))

if age > 21:
    print("Youare eligible to drink beer")
else:
    print("GET LOST!")
    

for x in range(5, 50, 10):
    print(x)

mine = int(input("Enter the value"))

while mine < 20:
    print(mine)
    mine +=1



for n in range(0,101):
    if n%4 is 0:
        print(n)
    

def trust():
    print("Heya, cool! Aren't you?")
    
def mm_into_cm(mm):
    size = mm * 100
    print(size)

mm = int(input("Enter length in mm"))  
trust()
mm_into_cm(mm)  




def allowed_driving_age():
    allowed_age = my_age/2 + 7
    return allowed_age
    
my_age = int(input("Enter your age"))
allowed_driving_age()
age = allowed_driving_age()

if my_age > age:
        print("Since you are", my_age,",", "which is >", age, " So, you are eligible to drive")


def health_calculator():
    answer = (100-age) + (apples * 3.5) - (cigs * 3)
    print(answer)
    
age = int(input("Enter your age"))
apples= int(input("Enter the no. of apples you eat in a week"))
cigs = int(input("Enter the no. of cigs you smoke in a week"))
health_calculator()




def health_calculator(age, apples, cigs):
    answer = (100-age) + (apples * 3.5) - (cigs * 3)
    print(answer)

me = [25, 3, 0]
health_calculator(*me)



country_names = ["AlBerta", "    CocoN", "Georgia", "georgia", "FlOrIda",
                 "south carolina##", "West virginia?"]

import re
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result

clean_strings(country_names)


float('1.2345')

import numpy as np
a = [7, 6.8999, 9, 10]
arr1 = np.array(a)
arr1
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
result = np.array(data2)
result
np.zeros((2, 10))
np.empty((3, 4, 3))
np.arange(35)

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
arr.dtype
float_arr = arr.astype(np.float64)
float_arr
float_arr.dtype

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
arr.astype(np.int32)
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_strings
numeric_strings.astype(float)

import numpy as np
arr = np.arange(10)
arr
arr[5]
arr[0:5]
arr[5:8] = 12
arr

arr_slice = arr[5:8]
arr_slice
arr_slice[1] = 1234567
arr

arr2d = np.array([[2, 1, 3], [3, 5, 7], [56, 78, 90]])
arr2d
arr2d[2, :].shape
arr2d[2:, :].shape

arr2d[1][1]
arr2d[1, 1]


data = np.random.randn(2, 3)
data

data1 = np.random.rand(2, 3)
data1
data1.dtype

numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_strings.astype(float)

come = np.array([[1, 2, 3], [345, 4, 444444], [222234, 456, 5555]])
come
come[0]
come[0] = 24
come

import numpy as np
sup = np.array(range(9))
sup
sup1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sup1
sup1[:2]
sup1[:2, 1:]
sup1[:1,1:]
sup1[:,:2]
sup1[:3, 1:] = 0
sup1


names = np.array(["bob", "Shreya", "Thomas", "John", "Shreya", "John", "bob"])
names
data = np.random.randn(7,4)
data
names == "Shreya"
data[names == "Shreya"]
data[names == "Shreya", 2:]

why = np.empty((8, 4))
why
for i in range(8):
    why[i] = i
    
why
why[[4, 5, 0, 7]]

arr = np.arange(32)
arr
arr = np.arange(32).reshape(8,4)
arr
arr[0]
arr[[2, 6, 4, 1], [1, 2, 2, 3]]  #index to view elements


arr2 = np.arange(15).reshape(5,3)
arr2
arr2.T

arr = np.random.randn(3, 5)
arr

matrix = np.arange(10)
matrix
np.sqrt(matrix)
np.exp(matrix)

x = np.random.randn(8)
y = np.random.randn(8)
x
y
np.maximum(x,y)
np.add(x,y)
np.subtract(x,y)
np.multiply(x,y)
np.divide(x,y)

arr = np.random.randn(7) * 5
arr
remainder, whole_part = np.modf(arr)
remainder
whole_part

import numpy as np
points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
xs
ys
z = np.sqrt(xs**2 + ys**2)
z

xarr = np.array([1.2, 1.3, 1.4, 1.5, 1.6])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, False, False, True])

result = [(x if c else y) for x,y,c in zip(xarr, yarr, cond)]
result

res = np.where(xarr, yarr, cond)
res


arr = np.random.randn(4,4)
arr
arr > 0
result = np.where(arr > 0, 2,-2)
result

#mean, mode, median

import numpy as np

arr = np.random.randn(5,4)
arr 
mean = np.mean(arr)
mean
arr.mean(axis = 0)
arr.sum(axis = 0)

#cumulative sum
arrat = np.array([0, 1, 3, 5, 67, 89, 100])
arrat.cumsum()

import numpy as np
ask = np.array(([1, 2, 3],[4, 5, 6], [7, 8, 9]))
ask
ask.cumsum()
ask.cumsum(axis = 0)
ask.cumsum(axis = 1)
ask.cumprod(axis = 0)

import numpy as np

ass = np.random.randn(5)
ass
ass.sort()
ass

asses = np.random.randn(5,3)
asses
asses.sort() # sorting whole array
asses
asses.sort(1) # sorting array at position 1
asses

large_arr = np.random.randn(1000)
np.sort(large_arr)
large_arr[int(0.5 * len(large_arr))]

#matrix dot multiplication

x = np.array([[6, 5, 3],[1, 2, 3]])
x
y = np.array([[1, 2], [4, 5], [7,9]])
y
x.dot(y) #normal method
np.dot(x,y)
np.dot(x, np.ones(3))

#inverse and transpose

from numpy.linalg import inv, qr
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat
x = mat.T.dot(mat) 
x
inv(x)


single_array = np.array([1.1, 2.1, 3.1])
np.sqrt(single_array)
single_array
np.sqrt(single_array, single_array)
single_array


lis = (1, 2, 3, 4)
shut = (4, 5, 6, 7)
for x,y in zip(lis,shut):
    print(x,y)



from random import normalvariate
N = 1000000
samples = [normalvariate(0, 1) for _ in range(N)]
samples














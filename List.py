# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 09:59:51 2018

@author: DELL
"""

kingName = input("Please type in your name at the prompt") 
numJewels = int(input("Hey" + kingName + " How many jewels do you have"))
costofjewels = int(input("How much do they cost"))
TotalPrizemoney = costofjewels * numJewels
print("TotalPrizemoney = ", TotalPrizemoney)
names = ["Shreya", "Priya", "Riya"]
ages = [25, 45, 34]
names.insert(0,"Prudhvi")
print("Names",names)
ages.append("27")
print("Ages",ages)
temp = names.pop(0)
names.append(temp)
print("Names = ", names)
print("Ages=", ages)
print("Total Number of people", str(len(names)))

names = ["Shreya", "Priya", "Riya"]
ages = [25, 45, 34]
kingName = input("Please type in your name at the prompt") 
galtokill = input("Hey, " + kingName + " Whom to kill?")

print ("Erasing all history of", names[int(galtokill)-1], " whose age is " ,ages[int(galtokill)-1])
del names[int(galtokill)-1]
del ages[int(galtokill)-1]




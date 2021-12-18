# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 16:42:48 2021

@author: gar20
"""

# Python Testing

# Assignments

print("Testing Anaconda")
data = 'Hello World'
print(data[0])
print(len(data))
print(data)

value = 123.1
print(value)
value = 10
print(value)

a = True
b = False
print(a, b)

a, b ,c = 1, 2, 3
print(a, b, c)

a = None
print(a, '\n')

# Flow control

value = 205

if value == 99:
    print('That is fast')
elif value > 200:
    print('That is too fast')
else:
    print('That is safe')
    
for i in range(2, 8):
    print(i)
    
print()
i = 0

while i < 10:
    print(i)
    i += 1
    
# Data Structures

print()
a = (1, 2, 3)
print(a)

myList = [1, 2, 3]
print("Zeroth value: %d" % myList[0])
myList.append(4)
print("List length: %d" % len(myList))
for value in myList:
    print(value)

print()
myDict = {'a': 1, 'b': 2, 'c': 3}
print("A value: %d" % myDict['a'])
myDict['a'] = 11
print("A value: %d" % myDict['a'])
print("Keys: %s" % myDict.keys())
print("Values: %s" % myDict.values())
for key in myDict.keys():
    print(myDict[key])
    
# Functions

def mySum(x, y):
    return x + y

result = mySum(1, 3)
print("\nSum = ", result, sep="")




















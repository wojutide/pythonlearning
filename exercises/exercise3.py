#!/usr/bin/python3.5

import sys

'''exercise 2

Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
'''
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]

for i in a:
    if i<5:
        b.append(i)
        print (i)
print(b)

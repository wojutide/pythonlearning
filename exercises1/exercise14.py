#!/usr/bin/python3.5

import sys

'''exercise 1
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
'''

def inp():
    L=[]
    name=input('Please input the element of the list("end" for ending): ')
    while name != 'end':
        L.append(name)
        name=input('Please input the element of the list("end" for ending): ')
    return L

def remove(L):
    return set(L)

L=remove(inp())
print (L)

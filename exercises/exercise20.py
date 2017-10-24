#!/usr/bin/python3.5

import sys

'''exercise 1
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

    Use binary search.
'''

def fun(L,num):
    return num in L

L=[1,2,3,45]

print(fun(L,1))
print(fun(L,100))

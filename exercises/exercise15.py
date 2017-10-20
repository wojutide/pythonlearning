#!/usr/bin/python3.5

import sys,re
from functools import reduce

'''exercise 1
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

      My name is Michele
      Then I would see the string:

        Michele is name My
        shown back to me.
'''

string=input('Please input a string: ')

def ssum(x,y):
    return x+' '+y


def invstring(string):
    string=re.split(r'\s+',string)
    return reduce(ssum, string[::-1])

def fun2(string):
    string=re.split(r'\s+',string)
    return ' '.join(string[::-1])

#print(invstring(string))
print(fun2(string))

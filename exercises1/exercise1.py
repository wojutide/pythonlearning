#!/usr/bin/python3.5

import sys

'''exercise 1

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.'''

name=input('Please input your name: ')
print('You name is %s' % name)
age=input('Please input your age: ')
print('You age is %s' % age)

try:
    age=int(age)
except:
    print ('Error occurs: your age is not integer')
    sys.exit()

def yearofage(n,age):
    print('The year now is 2017')
    return n-age+2017

print('By the year %d, you aget will be %d' % (yearofage(100,age), 100) )

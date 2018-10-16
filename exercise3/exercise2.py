#!/usr/bin/python3.5

from functools import wraps
import sys

'''
Write a decorator function which should only allow a function to have even parameters or else return the string "Please only use even numbers!"
'''

def num_of_args(func):
    def wrapper(*args,**kw):
        print(len(args)+len(kw))
        return func(*args,**kw)
    return wrapper

def decorate_even(func):
    def wrapper(*args,**kw): 
        l=len(args)+len(kw) 
        if l%2==0: 
            return func(*args,**kw)
        else:
            return 'Parameter no. not correct while open %s' % func.__name__
    return wrapper

@decorate_even
def f3(a,b,c=1):
    return a+b+c


@num_of_args
def f2(a,b):
    return a+b

print(f3(1,2))
print(f3(1,2,3))
print(f2(1,2))


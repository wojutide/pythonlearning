#!/usr/bin/python3.5

import sys
import functools

def decorate_args(method):
    @functools.wraps(method)
    def wrapper(self,*args,**kw):
        l=len(args)+len(kw)
        print("Number of argumens: %d " % l)
        return method(self,*args,**kw)
    return wrapper

class MyClass(object):
    def __init__(self,text):
        print(text)

    @decorate_args
    def prtage_args(self,*args,**kw):
        print(args)
        print(kw)
        

me=MyClass('Welcome')
me.prtage_args('What\'s your name?\n', 'Hao')

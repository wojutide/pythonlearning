#!/usr/bin/python3.5

from functools import wraps

'''
Write a Python program to make a chain of function decorators (bold, italic, underline etc.).
'''


def decorator_bold(func):
    @wraps(func)
    def wrapper(*args,**kw):
        print('Call %s()' % func.__name__)
        #return func(*args,**kw)
        return  '<b>' + func(*args, **kw) + '</b>'
    return wrapper

def decorator_italic(func):
    def wrapp(*args,**kw):
        return '<i>'+func(*args, **kw) + '</i>'
    return wrapp

def decorator_underline(func):
    def wrapp2(*args,**kw):
        return '<u>'+func(*args, **kw)+'</u>'
    return wrapp2

@decorator_underline
@decorator_italic
@decorator_bold
def fprt(string):
    print(string)


print(fprt('Test'))

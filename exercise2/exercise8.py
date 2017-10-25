#!/usr/bin/python3.5

import sys,re

'''
8. Write a Python class to reverse a string word by word. - Go to the editor
Input string : 'hello .py'
Expected Output : '.py hello'

Click me to see the solution
'''

class MyString(object):
    def __init__(self,string):
        self.string=string

    def str_ivs(self):
        return ' '.join(reversed(re.split(r'\s+',self.string)))

string='Mypython my god'
a=MyString(string)
print(a.string)
print(a.str_ivs())


#!/usr/bin/python3.5

import sys

'''
7. Write a Python class to implement pow(x, n). - Go to the editor

Click me to see the solution
'''


class mymath(object):
    def power(self,x,n):
        if n==1:
            return x
        else :
            return x*self.power(x,n-1)


print(mymath().power(3,4))


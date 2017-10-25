#!/usr/bin/python3.5

import sys
import re

'''
Write a Python class to get all possible unique subsets from a set of distinct integers.
'''

class MySet(object):
    
    def subset(self,L=[],Lsubs=[]):
        if len(L)==1:
            Lsubs.append(L)
        else:
            Lsubs.append(L)
            for i in L:
                Ltmp=[x for x in L if x != i]
                if Ltmp not in Lsubs: 
                    self.subset(Ltmp,Lsubs)
        Lsubs.sort(key=len)
        return Lsubs



L=re.split(r'\s+',input('Please input the list you want to search: ').strip())

print(MySet().subset(L))

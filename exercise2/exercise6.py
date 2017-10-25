#!/usr/bin/python3.5

import sys

'''
6. Write a Python class to find the three elements that sum to zero from a set of n real numbers. - Go to the editor
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
'''

class Mylist(object):
    def get_sum_zero(self,L):
        Lzero=[]
        for k, val1 in enumerate(L):
            for l,val2 in enumerate(L[k+1:]):
                if -val1-val2 in L[k+l+2:]:
                    Lzero.append([val1,val2,-val1-val2])
        return Lzero

L=[-25, -10, -7, -3, 2, 4, 8, 10]

print(Mylist().get_sum_zero(L))
                    


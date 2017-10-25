#!/usr/bin/python3.5

import sys

'''
 Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
'''

class StrbyPar(object):

    def FindString(self, string):
        Parentheses=[['(',')'],['[',']'],['{','}']]
        L=[]; i=0
        for x in string:
            for y in Parentheses:
                if x in y:
                    L.append([x,Parentheses.index(y)])
        
        while i<len(L):
            if L[i][1]==L[len(L)-i-1][1] and L[i][0] != L[len(L)-i-1][0]:
                i+=1 
            else:
                print('String invalid!')
                break
        if i==len(L):
            print('String valid!')


while True:
    string=input('Please input a string(Two enter to end the input): ')
    if string=='':
        sys.exit()
    else:
        StrbyPar().FindString(string)
        

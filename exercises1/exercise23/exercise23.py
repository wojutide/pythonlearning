#!/usr/bin/python3.5

import sys

'''exercise 1
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)
'''

def fread(filename):
    with open(filename,'r') as f:
        return f.readlines()

def comp(L1,L2):
    L=[]
    for i in L1:
        for j in L2:
            if i==j:
                L.append(i)
                L2.remove(i)
    return [x[:-1] for x in L]



if __name__=='__main__':
    L1=fread('1.dat')
    L2=fread('2.dat')
    print('common value:', comp(L1,L2))


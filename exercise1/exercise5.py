#!/usr/bin/python3.5

import sys, math

'''exercise 4

Take two lists, say for example these two:

      a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
'''

a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c=a
d=b
n=0
v=[]  # to store common number
for i in c:
    for j in d:
        print('i,j',i,j)
        if i == j:
            v.append(j)
            d.remove(j)
            break
        n=n+1

print(n)
print(v)
print('c:', c)
print('d:', d)

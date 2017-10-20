#!/usr/bin/python3.5

import sys, math

'''exercise 4
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

num=float(input('Please input a number: '))

b=int(math.sqrt(num))

primedata=[]
for i in range(2,int(num)):
    if num%i==0:
        primedata.append(i)

print(primedata)
        

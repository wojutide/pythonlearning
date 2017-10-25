#!/usr/bin/python3.5

import sys, math

'''exercise 4
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

def fp(num):
    primedata=[]
    for i in range(2,num):
        if num%i==0:
            primedata.append(i)
    if len(primedata) >0:
        print('The number you input is not prime, it has divisors:')
        print(primedata)
    else:
        print('The number you input is a prime')

def integer_get():
    return int(input('Please give me a integer: '))

num=integer_get()
fp(num)


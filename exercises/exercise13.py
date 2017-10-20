#!/usr/bin/python3.5

import sys

'''exercise 1

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

v=[]

def fab(num):
    if num==1 or num==2 :
        return 1
    else:
        return fab(num-1)+fab(num-2) 

a=int(input('Please input the number of numbers in the sequence: '))

print('The number is: %d' % fab(a))
print(v)

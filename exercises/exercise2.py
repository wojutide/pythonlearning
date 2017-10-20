#!/usr/bin/python3.5

import sys

'''exercise 2

Ask the user for a number.  Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?
'''

num=int(input('Please input an integer to see whether it can be devided by 2: '))

if num%2==1:
    print( 'Can not be divided by 2')
else:
    print('Can be devided by 2')

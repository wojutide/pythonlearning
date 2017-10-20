#!/usr/bin/python3.5

import sys, math

'''exercise 6

Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

string=input('Please input a string to test wether it is a palindrome: ')

string2=''

for i in string:
    string2=i+string2

if string2==string:
    print('Palindrome')
else:
    print('Not palindrome')

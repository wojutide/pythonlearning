#!/usr/bin/python3.5

import sys
import random

'''exercise 1
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

lower=list(map(chr,range(ord('a'),ord('z'))))
upper=list(map(chr,range(ord('A'),ord('Z'))))
number=list(map(chr,range(ord('0'),ord('9'))))
letter=lower+upper+number

def pwdgen(num,num2,num3):
    i=0; j=0; k=0
    while True:
        chr1=random.choice(letter)
        if chr1 in lower and i<num :
            i+=1
            yield chr1
        elif chr1 in upper and j<num2 :
            j+=1
            yield chr1
        elif chr1 in number and k<num3 :
            k+=1
            yield chr1
        elif i+j+k == num+num2+num3:
            break
        else:
            continue

def pw(num1,num2,num3):
    pwd=''
    for ch in pwdgen(num1,num2,num3):
        pwd=pwd+ch
    return pwd

num1=int(input('Please input how many lowercase letters you want to input: '))
num2=int(input('Please input how many uppercase letters you want to input: '))
num3=int(input('Please input how many number letters you want to input: '))

pwd=pw(num1,num2,num3)
print(pwd)


#!/usr/bin/python3.5

import sys
import random

'''exercise 1
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

def pwdgen(num):
    i=0
    while i<=num:
        num=random.randint(1,128)
        i += 1
        yield chr(num)
    return 'done'

def pw(num):
    pwd=''
    n=0
    for ch in pwdgen(num):
        pwd=pwd+ch
    print(pwd)
    return pwd

pwd=pw(10)
print(pwd)


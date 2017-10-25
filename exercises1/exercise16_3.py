#!/usr/bin/python3.5

import string
import random

'''exercise 1
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

def pwdgen(size=8, char=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(char) for i in range(size))

print(pwdgen(int(input('Please input the number of characters in your password: '))))

#!/usr/bin/python3.5

import sys, math
import random 

'''exercise 9

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
'''

num=random.randint(1,9)

def cpr(num, num_user,n):
    if num==num_user:
        print('Congratulations, you are right!')
        print('The times you use: %d' % n)
        sys.exit()
    elif num < num_user:
        print('Your number are too large')
    else:
        print('Your number are too small')

n=0
while True:
    string=input('Please input your guess of the number or exit to exit: ')
    if string == 'exit' :
        sys.exit()
    else:
        num_user=int(string)
        n=n+1
        cpr(num,num_user,n)



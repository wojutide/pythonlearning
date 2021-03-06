#!/usr/bin/python3.5

import sys, string
import random

"""
Create a program that will play the “cows and bulls” game with the user. The game works like this:
    Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the
    user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed
    correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many
    “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track
    of the number of guesses the user makes throughout teh game and tell the user at the end.
    Say the number generated by the computer is 1038. An example interaction could look like this:
          Welcome to the Cows and Bulls Game!
          Enter a number:
                >>> 1234
                2 cows, 0 bulls
                >>> 1256
                1 cow, 1 bull
                ...
"""

num=''.join([random.choice('123456789')]+random.sample(string.digits,3))

def judge(val,num):
    cow=0; bull=0
    for i in range(len(val)):
        if val[i] == num[i]:
            cow+=1
        if val[i] in num and val[i] != num[i]:
            bull+=1
    return cow, bull


if __name__=="__main__":
    while True:
        val=input('please input a four-digit number as your guess("exit" to give up): ')
        [cow,bull]=judge(val,num)
        if cow==4 and bull==0 :
            print('You got %s cows %s bulls' %(cow, bull))
            print('Congratulations, you win!')
            print('The number is: %s' % num)
            sys.exit()
        elif val=='exit':
            print('You lose!')
            print('The number is: %s' % num)
            sys.exit()
        else:
            print('You got %s cows %s bulls' %(cow, bull))

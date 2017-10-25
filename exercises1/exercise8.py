#!/usr/bin/python3.5

import sys, math

'''exercise 7

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
'''


option={1:'rock', 2: 'scissors', 3:'Paper'}

def f(key1, key2):
    if int(key1) < int(key2) and int(key2)-int(key1) == 1 or int(key1)-int(key2)==2:
        print('player1 is the winner. Congratulation!' )
    elif key1==key2 :
        print('They are equal')
    else:
        print('player2 is the winner. Congratulations!')


while True:
    st=input('Do you want to start a new game?(yes/no): ')
    if st[0] in ['Y', 'y']:
        p1=input('Player 1 please input 1:rock, 2: scissors, 3:Paper: ')

        if int(p1) not in option.keys():
            print('Error of input')
            sys.exit()
        else:
            print('Your input is: %s' % option[int(p1)])

        p2=input('Player 2 please input 1:rock, 2: scissors, 3:Paper: ')
        if int(p2) not in option.keys():
            print('Error of input')
            sys.exit()
        else:
            print('Your input is: %s' % option[int(p2)])

        f(p1,p2)
    else:
        break



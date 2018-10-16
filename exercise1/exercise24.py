#!/usr/bin/python3.5

import sys

'''exercise 1
his exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

     --- --- --- 
     |   |   |   | 
      --- --- ---  
      |   |   |   | 
       --- --- ---  
       |   |   |   | 
        --- --- --- 
        This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

        Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

        Remember that in Python 3, printing to the screen is accomplished by

          print("Thing to show on screen")
          Hint: this requires some use of functions, as were discussed previously on this blog and elsewhere on the Internet, like this TutorialsPoint link.
'''

def ptn(ch1, ch2, wd1=1,wd2=3):
    s=''
    for i in range(wd1):
        s=s+ch1
    for j in range(wd2):
        s=s+ch2
    return s


def hz_line(n,s,string=''):
    if n==1:
        return string+s
    else:
        n-=1
        return hz_line(n,s,string=string+s)


def bd_draw(n,ch1='-',ch2='|'):
    for i in range(n):
        print(hz_line(n,ptn(' ',ch1)))
        print(hz_line(n,ptn(' ',' ')))
        print(hz_line(n,ptn(ch2,' '))+ch2)
        print(hz_line(n,ptn(' ',' ')))
    print(hz_line(n,ptn(' ',ch1)))

if __name__=='__main__':
    n=int(input('Please input the size of the table you want to produce: '))
    yorn=input('Do you want to input the the pattern of the border?(yes/no)\n')
    if yorn=='yes':
        ch1=input('Please input the pattern of horizontal border: ')
        ch2=input('Please input the pattern of vertical border: ')
        bd_draw(n,ch1,ch2)
    else:
        bd_draw(n)


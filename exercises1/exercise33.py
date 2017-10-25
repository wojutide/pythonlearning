#!/usr/bin/python3.5

import sys

'''exercise 1
This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are: Part 2, Part 3, and Part 4.

For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. The interaction should look something like this:

    >>> Welcome to the birthday dictionary. We know the birthdays of:
        Albert Einstein
        Benjamin Franklin
        Ada Lovelace
        >>> Who's birthday do you want to look up?
        Benjamin Franklin
        >>> Benjamin Franklin's birthday is 01/17/1706.
        Happy coding!
'''

def fread(filename):
    D={}
    with open(filename,'r') as f:
        Data=f.readlines()
    for dat in Data:
        if not dat:
            D[dat.split(':')[0].strip()]=dat.split(':')[1].strip()
    return D


def fwrite(filename,D): # D as a dictionary
    with open(filename,'a+') as f:
        for k, v in D.items():
            f.write('%s: %s\n' %(k , v))

def prtall(D):
    print('Welcom to the birthday dictiondary. We knows the birthdays of:\n ')
    for k, v  in D.items():
        print('%s' %k)


if __name__=='__main__':

    filename="birthday.dat"
    D=fread(filename)
    prtall(D)

    while True:
        jd=input('Please input the information (format: name:birthdays or end): ')
        if jd=='end':
            print('Now we have these information:')
            prtall(D)
            sys.exit()
        else:
            k=jd.split(':')[0].strip()
            v=jd.split(':')[1].strip()
            print('You add %s\'s birthday information: %s' %(k,v))
            fwrite(filename,{k:v})


#!/usr/bin/python3.5

import sys
import json
from collections import Counter

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
    try:
        with open(filename,'r') as f:
            Data=json.load(f)
    except:
        print("File not exist! I will creat a new one!") 
        f=open(filename,'w')
        Data={}
        f.close()
    return Data



def fwrite(filename,Djson): # Djson as a Json format file
    with open(filename,'w') as f:
        json.dump(Djson, f)


def prtall(Djson,flag=1):
    print('Welcom to the birthday dictionary. We knows the birthdays of: ')
    if Djson and flag==1: 
        for k, v  in Djson.items(): 
            print('%s' %k)
    elif Djson and flag != 1: 
        for k, v in Djson.items():
            print('%s: %s' %(k,v))
    else:
        print('No data!')

def chk(Djson,key):
    if key in Djson:
        print('The birthday of %s is: %s' % (key,Djson[key]))
    else:
        print('No data!')


def birthinput(Djson):
    while True:
        jd=input('Please input the information (format: name:yyyy-mm-dd or end): ')
        if jd=='end':
            return Djson
        else:
            k=jd.split(':')[0].strip()
            v=jd.split(':')[1].strip()
            if k in Djson.keys():
                print('You have updated %s\'s information!' % k) 
            else:
                print('You add %s\'s birthday information: %s' %(k,v))
            Djson[k]=v


def birthcounter(Djson,n): # n=1: yyyy to count, n=2: mm to count, n=3: dd to count
    Mon={1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
    L=[]
    for k, v in Djson.items():
        if len(v.split('-'))>n-1 and n!=2 : 
            L.append(v.split('-')[n-1])
        elif len(v.split('-')) > 1 and n==2:
            L.append(Mon[int(v.split('-')[1])])
        else:
            print('%s\'s data is not enough!' % k)
    print(Counter(L))


if __name__=='__main__':

    filename="birthday.json"
    Djson=fread(filename)
    prtall(Djson)

    while True:
        job=input('What do you want to do?(Input: I, Search: S, Counte: C or end: E): ')
        if job=='I':
            Djson=birthinput(Djson)
            print('Now we have these information:')
            prtall(Djson,2)
            fwrite(filename,Djson)
        elif job=='S':
            key=input('The name of the people you want to check: ')
            key=key.strip()
            chk(Djson,key) 
        elif job=='C':
            bc=birthcounter(Djson,n=2)
        else:
            sys.exit()



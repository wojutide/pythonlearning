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
    try:
        with open(filename,'r') as f:
            Data=f.readlines()
    except:
        print("File not exist! I will creat a new one!") 
        f=open(filename,'w')
        Data=''
        f.close()

    D={}
    for dat in Data: 
        if dat: 
            D[dat.split(':')[0].strip()]=dat.split(':')[1].strip() 
    return D



def fwrite(filename,D): # D as a dictionary
    with open(filename,'w') as f:
        for k, v in D.items():
            f.write('%s: %s\n' %(k , v))

def prtall(D,flag=1):
    print('Welcom to the birthday dictionary. We knows the birthdays of: ')
    if D and flag==1: 
        for k, v  in D.items(): 
            print('%s' %k)
    elif D and flag != 1: 
        for k, v in D.items():
            print('%s: %s' %(k,v))
    else:
        print('No data!')

def chk(D,key):
    if key in D:
        print('The birthday of %s is: %s' % (key,D[key]))
    else:
        print('No data!')

def birthinput():
    while True:
        jd=input('Please input the information (format: name:birthdays or end): ')
        if jd=='end':
            return D
        else:
            k=jd.split(':')[0].strip()
            v=jd.split(':')[1].strip()
            if k in D.keys():
                print('You have updated %s\'s information!' % k) 
            else:
                print('You add %s\'s birthday information: %s' %(k,v))
            D[k]=v




if __name__=='__main__':

    filename="birthday.dat"
    D=fread(filename)
    prtall(D)

    job=input('What do you want to do?(input data: I or check: C): ')
    if job=='I':
        D=birthinput()
        print('Now we have these information:')
        prtall(D,2)
        fwrite(filename,D)
    else:
        key=input('The name of the people you want to check: ')
        key=key.strip()
        chk(D,key)



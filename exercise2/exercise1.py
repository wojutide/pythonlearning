#!/usr/bin/python3.5

import sys

'''
 Python class to convert an integer to a roman numeral.
'''

class NumProc(object):
    def __init__(self,num):
        self.num=num

    def num_to_rom(self):

        Rom = [[1,'I'],
                [4,'IV'],
                [5,'V'], 
                [9,'IX'], 
                [10,'X'], 
                [50,'L'], 
                [90,'XC'], 
                [100,'C'], 
                [400,'CD'], 
                [500,'D'], 
                [900,'DM'], 
                [1000,'M']]
        n=len(Rom)
        L=[]
        while n >0 and self.num>0 :
            quo=self.num//int(Rom[n-1][0])
            if quo != 0:
                for _ in range(quo):
                    L.append(Rom[n-1][1]) 
            self.num=self.num % int(Rom[n-1][0])
            n-=1

        Srom=''
        for i in range(len(L)):
            Srom=Srom+L[i]
        return Srom
        
        




if __name__=='__main__': 
    num=int(input('Please input a integer(less than 4000): ')) 
    a=NumProc(num)
    print(a.num_to_rom())

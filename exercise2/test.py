#!/usr/bin/python3.5
import sys
import re
def getsubset(L=[],Lsubs=[]):
    if len(L)==1:
        Lsubs.append(L)
    else:
        Lsubs.append(L)
        for i in L:
            Ltmp=[x for x in L if x != i]
            if Ltmp not in Lsubs:
                getsubset(Ltmp,Lsubs)
    
    return Lsubs


print(getsubset([1,2,3]))

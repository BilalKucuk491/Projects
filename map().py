# -*- coding: utf-8 -*-
"""
Created on Thu May 21 12:51:50 2020

@author: BİLAL
"""


def kare(a):
    return a**3
def dene(b):
    return b*2 

print(list(map(kare,[0,1,2,3,4,5,6,7,8,9,9.9])))
print(list(map(dene,["ali","veli","49","50"])))

print(list(map(lambda x : x**2,[1,2,3,4,5] )))

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:37:06 2020

@author: BİLAL
"""


def yan_kare(adet):
    for i in range(int(adet)):
        print("#",end="")
        

def ust_kisim(cap):
    for i in range(int(cap/2)):
        yan_kare(1)
        
        
print(ust_kisim(8))       
            
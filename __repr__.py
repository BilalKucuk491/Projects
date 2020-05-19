# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:46:48 2020

@author: BİLAL
"""
import datetime as zaman


class hello:
    def toplat(a,b):
        return a + b
    
    
    def __repr__(self):
        return "Selam"
    
    
hi = hello()
print(hi.__repr__())    
#print(str(hi))

print(int.__add__(5,1))
print(str.__add__("5","Five"))
bugun = zaman.date.today()
print(repr(bugun))

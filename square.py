# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:37:06 2020

@author: BİLAL
val= value
r = diameter
"""

class Square:
    
    def side_square(val):
        for i in range(int(val)):  
         print("#",end="")
        
    def top_square(r):
        
        for i in range(int(r/2)):
            
            side_square(1)
        
        
print(top_square(8))       
            

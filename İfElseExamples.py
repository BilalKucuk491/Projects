# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:57:35 2020

@author: BİLAL

Square-Pyramid 
Total Surface Area of a square pyramid

a*((4*h**2 + a**2)**0.5 + a))
a = side length
h = height
     
"""

a = int(input("Side Lenght: "))
h = int(input("Height: "))
total_area = a*((4*h**2 + a**2)**0.5 + a)
print("Total surface area of square pyramid: {}".format(total_area))
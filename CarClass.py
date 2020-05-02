# -*- coding: utf-8 -*-
"""
Created on Sat May  2 13:56:29 2020

@author: BİLAL


class Car:
    color = "Gray"
    cylinder = 4
    model = "Tesla"
    plaka = "07 Antalya F21"

car1 = Car()
print(car1.color)  
car2 = car1
print(car2.plaka) 
"""

class car():
 
    def __init__(self,color,cylinder,model):
        self.r = color
        self.c = cylinder
        self.m = model
        print("Fuck you")

car1 = car("Blue",4,"Toronto")

        
        
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:52:42 2020

@author: BİLAL

Total surface area of cylinder  = 2.pi.r.h + 2.pi.r.r ya da 2.pi.r(h+r)
h = height,r=diameter,pi= 3

cylinder volume formula = pi.r.r.h
"""
cy_height = int(input("Cylinder Height: "))
cy_diameter = int(input("Cylinder Diameter: "))
pi = 3
cy_area = str(2*pi*cy_diameter*(cy_height+cy_diameter))
cy_volume = str(pi*cy_diameter*cy_diameter*cy_height)

print("Total area of cylinder: ",cy_area)
print("Total volume of cylinder : ",cy_volume)

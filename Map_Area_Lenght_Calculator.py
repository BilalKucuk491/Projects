# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:24:48 2020

@author: BİLAL

real length = RL
map lenght = ML
denominator of the scale = DS

# RL = ML X DS
real_lenght = int(input("Enter a Real lenght: "))
map_lenght = int(input("Enter a Map lenght: "))
DS = int(input("Enter a DS: "))
           
while True:  
    if real_lenght == 0:
      real_field(1)
    elif map_lenght == 0:
      map_lenghtt(1)
    elif DS == 0:
       map_DS(1)
    else:
      print("Error 404")

      
"""


menu = """

[1] Real lenght Calculator
[2] Map lenght Calculator
[3] DS lenght Calculator
[q] Quit

"""
# Map area calculator

def real_field(num):
    map_lenght = int(input("Map lenght: "))
    DS = int(input("DS: "))
    return  map_lenght * DS
    

    
def map_lenghtt(num):
    real_lenght = int(input("Real lenght: "))
    DS = int(input("DS: "))
    return real_lenght / DS
    

def map_DS(num):
    real_lenght = int(input("Real lenght: "))
    map_lenght = int(input("Map lenght: "))
    return real_lenght / map_lenght 
    

while True:
   print(menu)
   selection = input("You are selection ")

   if selection == "1":
       print(real_field(1))
       print("\nEnter for menu")
       input()
       
   elif selection == "2":
       print(map_lenghtt(1))
       print("\nEnter for menu")
       input()
       
   elif selection == "3":
       print(map_DS(1))
       print("\nEnter for menu")
       input()
       
   elif selection == "q" or selection == "Q":
       quit(1)
   else:
       print("Error 404")

       
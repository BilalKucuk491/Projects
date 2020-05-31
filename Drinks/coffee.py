# -*- coding: utf-8 -*-
"""
Created on Sun May 31 13:49:06 2020

@author: BİLAL
version 1.0
try it very easy.
"""

from sqlCommant import sqlCo
import time

def interface():
    print("""
                  
            1)Create table
            2)Add table
            3)Show on table
            4)Update Table
            5)Delete column
            6)EXİT
                  """)  

def dodnet():
    for i in range(3): 
                print(".",end="")
                time.sleep(1)            
while 1:
    try:
        menu = input("You are selection exit : 0 next : 1 ")
        if menu == "1":
            dodnet()
                
            interface()
            selection = int(input("You are selection: "))
            
            if selection ==1:
                sqlCo.create_tble()
                
            elif selection == 2:
                d_name = input("Drink Name: ")
                price = int(input("Drink Price: "))
                piece = int(input("Drink Piece: "))
                sqlCo.add_tble(d_name, piece, price)
                
            elif selection == 3:
                sqlCo.showOn_tble()
            elif selection == 4:
                
                old_price = int(input("Old Drink price: "))
                new_price = int(input("New Drink price: "))
                sqlCo.update_tble(old_price, new_price)
                
            elif selection == 5:
                d_name = input("Drink Name: ")
                sqlCo.delete_column_tble(d_name)
                dodnet()
                print("Delte column = {}".format(d_name))            
        else:
            break
    except ValueError:
        print("Value Type Error")    
   

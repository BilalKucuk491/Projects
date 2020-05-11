# -*- coding: utf-8 -*-
"""
Created on Mon May 11 21:29:33 2020

@author: BİLAL

what day were you born in the future
I will code showing.
        
"""

# Coding that I chose to find the central days.
    
def CenterDay(Year):
    day = int(input("Enter a year 1600 to 2100 : "))
    days = ["Sunday",0,"Monday",1,"Thuesday",2,"Wednesday",3,"Thursday",4,"Friday",5,"Saturday",6]
    
    Th1600 = 4
    Th1700 = 0
    Th1800 = 10
    Th1900 = 6
    Th2000 = 4
    Th2100 = 0
    
    if day >= 1600 and day < 1700:
        print(days[Th1600+1],days[Th1600])      
    elif day >= 1700 and day < 1800:
        print(days[Th1700+1],days[Th1700])      
    elif day >= 1800 and day < 1900:
        print(days[Th1800+1],days[Th1800])      
    elif day >= 1900 and day < 2000:
        print(days[Th1900+1],days[Th1900])      
    elif day >= 2000 and day < 2100:
         print(days[Th2000+1],days[Th2000])      
    elif day >= 2100 and day < 2200:
        print(days[Th2100+1],days[Th2100])       
    else:
        print("Error")
    return day    

CenterDay(1)

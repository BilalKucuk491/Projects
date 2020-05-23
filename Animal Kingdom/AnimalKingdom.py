# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:14:11 2020
@author: BİLAL
***********
Version 1.2.
***********
"""
  
class invertebrates(): 
    
    def sponges(): 
       with open("sponges.txt","r") as sponge:
               print(sponge.read())
             
    def solent(): 
         with open("solen.txt","r") as solen:
             print(solen.read())
             
    def worms(): 
        with open("worm.txt","r") as worm:
            print(worm.read())
       
    def molluscs(): 
        with open("mollusc.txt","r") as mollusc:
            print(mollusc.read())
    
    def arthropod(): 
        
        with open("arth.txt","r") as arth:
            print(arth.read())
        
    def echinoderm(): #Derisi Dikenliler
        with open("echino.txt","r") as echino:
            print(echino.read())


class vertebrates():
    
    def fishes(): 
        with open("fish.txt","r") as fish:
            print(fish.read())
            
    def two_Living(): 
        with open("frog.txt","r") as frog:
            print(frog.read())
            
    def reptiles(): 
        with open("reptile.txt","r") as reptile:
            print(reptile.read())  
            
    def birds(): 
        with open("bird.txt","r") as bird:
            print(bird.read())
            
    def mammals(): 
        
        with open("mammal.txt","r") as mammal:
            print(mammal.read())
            
while True:
    
    print("""
              
         1)Read
         2)Write
         0)Exit
   """)
    v = int(input("Select a number : "))
    if v == 1:
        
        print("""
                  
        1)Invertebrates
        2)Vertebrates
        0)Exit
        """)
            
        v1 = int(input("You are selection : "))
        if v1 == 1: 
            
            print("""      
            1)Sponges
            2)Solent
            3)Worms
            4)Molluscs
            5)Arthropod
            6)Echinoderm
                
            exit = 0
            """)
            v2 = int(input("You are selection : "))
            if v2 == 1:
                invertebrates.sponges()
            elif v2 ==2:
                invertebrates.solent()
            elif v2 == 3:
                invertebrates.worms()
            elif v2 == 4:
                invertebrates.molluscs()  
            elif v2 == 5:
                invertebrates.arthropod()
            elif v2 == 6:
                invertebrates.echinoderm() 
            else:
                break
        if v1 == 2: 
            
            print("""      
            1)Fishes
            2)Two-Living
            3)Reptiles
            4)Birds
            5)Mammals
                
            exit = 0
            """)
            v2 = int(input("You are selection : "))
            if v2 == 1:
                vertebrates.fishes()
            elif v2 ==2:
                vertebrates.two_Living()
            elif v2 == 3:
                vertebrates.reptiles()
            elif v2 == 4:
                vertebrates.birds  
            elif v2 == 5:
                vertebrates.mammals()
            else:
                break   
    elif v == 2:
        pass
    else:
        break
    
        
               

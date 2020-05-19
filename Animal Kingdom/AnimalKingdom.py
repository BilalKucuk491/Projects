# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:14:11 2020

@author: BİLAL
Version 1.0
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
        
        
vertebrates.mammals()

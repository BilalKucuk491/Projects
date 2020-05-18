# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:14:11 2020

@author: BİLAL
"""

class invertebrates(): #Omurgasızlar
    
    def sponges(): #Süngerler
       with open("sponges.txt","r") as sponge:
               print(sponge.read())
             
    def solent(): #Sölenterler
         with open("solen.txt","r") as solen:
             print(solen.read())
             
    def worms(): #Solucanlar
        with open("worm.txt","r") as worm:
            print(worm.read())
       
    def molluscs(): #Yumuşakçalılar
        with open("mollusc.txt","r") as mollusc:
            print(mollusc.read())
    
    def arthropod(): #Eklem Bacaklılar
        
        with open("arth.txt","r") as arth:
            print(arth.read())
        
    def echinoderm(): #Derisi Dikenliler
        with open("echino.txt","r") as echino:
            print(echino.read())


class vertebrates(): #Omurgalılar
    
    def fishes(self): #Balıklar
        pass
    def two_Living(self): #İki Yaşamlılar
        pass
    def birds(self): #Kuşlar
        pass 
    def mammals(self): #Memeliler
        
        def beaked_Mammals(self): #Gagalı Memeliler
            pass 
        def marsupial_Mammals(self): #Keseli Memeliler
            pass 
        def plecantel_Mammals(self): #Plesantalı Memeliler
            pass 
        
        
invertebrates.echinoderm()
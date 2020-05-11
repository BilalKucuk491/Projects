# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:03:37 2020

@author: BİLAL


Allelic of rabbit to inheritance


You are try.
"""

print("""
      
      Rabbits:
          
      1) Albino 
      2) Himalayan 
      3) Chinchilla 
      4) Aguti 
    
      Rabbit dominantion
      Aguti > Chinchilla > Himalayan > Albino
      """)
      
MaleR = int(input("Male rabbit point : "))
FemaleR = int(input("Female rabbit point : "))
    
def dominantRabbit(MaleR,FemaleR):
   
    if FemaleR == 4 and MaleR == 3 or FemaleR == 3 and MaleR == 4 :
        print("3 Aguti"," 1 Chinchilla")
    elif FemaleR == 3 and MaleR == 2 or FemaleR == 2 and MaleR == 3 :    
        print("3 Chinchilla"," 1 Himalayan")
    elif FemaleR == 2 and MaleR == 1 or FemaleR == 1 and MaleR == 2 :    
        print("3 Himalayan"," 1 Albino")
    elif FemaleR == 1 and MaleR == 1:    
        print("4 Albino")
    elif FemaleR == 2 and MaleR == 2:     
        print("4 Himalayan")
    elif FemaleR == 3 and MaleR == 3:     
        print("4 Chinchilla")
    elif FemaleR == 4 and MaleR == 4:     
        print("4 Aguti")    
    else:
        print("Error :(")

dominantRabbit(MaleR, FemaleR)        
          
      


      

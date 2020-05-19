# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:31:12 2020

@author: BİLAL

"""

while True:
   try:
      
      kontrol = input("Quit for q ")
      if kontrol == "q":
          break
      num1 = int(input("Enter a number "))
      num2 = int(input("Enter a number "))
      
      print("\a \nNumber1 + Number2 = %s"%(num1+num2))  
      #print("Number1 + Number2 = {}".format(num1+num2))  
   except (ValueError,ZeroDivisionError):
        print("Type Error")
    
    #--------------------------------------------------
        
        
while True:
   try:
      
      kontrol = input("Quit for q ")
      if kontrol == "q":
          break
      num1 = int(input("Enter a number "))
      num2 = int(input("Enter a number "))
      
      print("\a \nNumber1 + Number2 = %s"%(num1+num2))  
      #print("Number1 + Number2 = {}".format(num1+num2))  
   except:
        print("Type Error")
   finally: 
       print("Hi")
       
      #----------------------------------------------- 
def summ(liste):
    if type(liste) == list or type(liste) == tuple:
       Sum = 0
       for s in liste:
           Sum +=s
       return Sum
    else:
        raise ValueError("Error")
#print(summ((1,2,3,4,5,6,7,8,9,10)))   
print(summ(("Aducet")))   # This is console say 'Error'


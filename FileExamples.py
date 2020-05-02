# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:23:08 2020

@author: BİLAL
print(document.read())

"""

document = open("TesteF.txt","r")
print(document.readlines())
print(document.readline())
print(document.read())
document.close()

with open("TesteF.txt","r") as dosya:
   dosya.seek(11) 
   print(dosya.read())
   
with open("TesteF.txt","a") as dosya:
   dosya.write("If you lov K-Pop, who is your favorite singer ?\n")
   print(dosya)   

with open("TesteF.txt","r+") as dosya:
   data = dosya.readlines()
   data.insert(5,"My favorite singer Lee Teamin.")
   dosya.seek(0)
   dosya.writelines(data)

    
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:27:05 2020

@author: BİLAL

def summ(a,b):
    return a+b
 
print(summ(5,6))

a = int(input("1.Sayı gir: "))
b = int(input("2.Sayı gir: "))

def summ(a,b):
    print(a*b)
summ(a,b)

Bir sayının karekökünü alma    

x=int(input("Karekök almak istediğiniz sayıyı gir: "))
def karekok(x):
    return x**0.5

def karesi(x):
    return x**2

print(karekok(x))
  
def fonksiyon(sayi):
    liste = [x for x in range(20) if x % sayi ==0]
    print(liste)
fonksiyon(5)    


def sayi_ekleme(x):
    liste = [1,2,3,4,5,6,7,8]
    liste.append(x)
    print(liste)
    
x = int(input("Sayı eklemek için sayı gir: "))        
sayi_ekleme(x)    
print(type(sayi_ekleme))
"""

def function(*args):
    summ=0
    for i in args:
        summ+=i
    return summ
    
print(function(1,2,3,4,5,6,7,8,9))



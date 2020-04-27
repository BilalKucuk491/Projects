# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:53:54 2020

@author: BİLAL

y =["Ali",1,12.4,"Elma",False]
a = False in y
print(a)

liste = [1,2,3,4,5]
for a in liste:
    print(a)
    
dene = ("John",12.5,15,True)
for x in dene:
    print(x)    

dene = int(input("Sayı giriniz: "))
toplam = 
for x in dene:
    toplam += x
print(toplam)    

print("Faktöriyel Hesaplama")
sayi = (1,2,3,4,5,6,7,8,9)
fak = 1
for x in sayi:
    fak = x*fak 
print("{}! = {}".format(sayi,fak))

dene = (1,2,3,4,5,6,7,8,9,10)
toplam = 0
for x in dene:
    if x %2 == 1:
        toplam +=x
print(toplam)   

sayilar = [(1,5),(2,6),(3,7),(4,8)]
for x,y in sayilar:
    print(x,y) 

sozluk = {"Apple": "Elma","Computer":"Bilgisayar","Tree":"Ağaç","Chocolate":"Çikolata"}
for a in sozluk.keys():
    print(a)
"""   
sayilar = range(0,100)
topla = 0
for x in sayilar:
    topla +=x
print(topla) 
a = (100*99)/2
print(a)   
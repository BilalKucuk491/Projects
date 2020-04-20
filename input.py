# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:56:43 2020

@author: BİLAL



dosya = open("deneme.txt","w+")
print(*"Deneme oldu",file=dosya)
dosya.close()

sayi = int(input("1.sayıyı gir "))
sayi2 = int(input("2. sayı gir ")) 
print("{} ile {}'nin toplamı {}'dir.".format(sayi,sayi2,sayi+sayi2))

sayi=input("0 ya da 1 giriniz: ")
print(bool(sayi))

sayi=float(input("1.Sayı : "))
sayi1=float(input("2.Sayı : "))
print("=o="*12)
print("Sayıların toplamı   : ",sayi+sayi1)
print("Sayıların çarpımı   : ",sayi*sayi1)
print("Sayıların bölümü    : ",sayi/sayi1)
print("Sayıların çıkarması : ",sayi-sayi1)
print("Sayıların modu      : ",sayi%sayi1)
print("=o="*12)
"""
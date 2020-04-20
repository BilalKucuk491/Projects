# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:32:30 2020

@author: BİLAL
"""
print("""
Seçimler;
[0] Toplama
[1] Çıkarma
[2] Çarpma
[3] Bölme
[4] Çıkış

Lütfen 1.Sayıya büyük olan sayı giriniz..
    """)

secim = float(input("Seçiminiz:  "))
sayi1 = float(input("1.Sayı: "))
sayi2 = float(input("2.Sayı: "))
if secim == 0 : 
    print("\nToplamı : {}".format(sayi1+sayi2))
elif secim == 1:
    print("\nÇıkarma : {}".format(sayi1-sayi2))
elif secim == 2: 
    print("\nÇarpma : {}".format(sayi1*sayi2))
elif secim == 3:
    print("\nBölme : {}".format(sayi1/sayi2))
elif secim == 4:
    print("Çıktın")
else:
    print("Hello")
        
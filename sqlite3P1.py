# -*- coding: utf-8 -*-
"""
Created on Sat May 30 13:16:48 2020

@author: BİLAL
"""


import sqlite3

baglanti = sqlite3.connect("personel.db")
isaretci = baglanti.cursor()

def tablo_olustur():
    isaretci.execute("create table if not exists ogrenciler(isim TEXT,soyad TEXT,maas İNT)")
    baglanti.commit()

def tablo_veri_ekleme(isim,soyad,maas):
    #isaretci.execute("insert into ogrenciler values('Aysel','Kurşun',7000 )")
    #isaretci.execute("insert into ogrenciler values('{}','{}',{})".format(isim,soyad,maas)) 
    isaretci.execute("insert into ogrenciler values(?,?,?)",(isim,soyad,maas)) 
    baglanti.commit()
    
tablo_olustur()  
isim = input("Adınız : ")
soyad = input("Soyadınız : ")
maas = input("Maaşınız : ")
tablo_veri_ekleme(isim,soyad,maas)

baglanti.close()
   
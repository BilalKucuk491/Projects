# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:38:37 2020

@author: BİLAL
"""


import sqlite3
baglanti = sqlite3.connect("sirket.db")
imlec = baglanti.cursor()

def tablo_olustur():
    imlec.execute("create table if not exists calisanlar (isim TEXT,soyad TEXT, yas INT,cinsiyet TEXT,posizyon TEXT, maas INT)")
    baglanti.commit()
    
def tablo_veri_ekleme(isim,soyad,yas,cinsiyet,posizyon,maas):
    imlec.execute("insert into calisanlar values (?,?,?,?,?,?)",(isim,soyad,yas,cinsiyet,posizyon,maas)) 
    baglanti.commit()

def tablo_veri_cek():
    imlec.execute("select * from calisanlar")
    veriler = imlec.fetchall()
    for i in veriler:
        print(i)

tablo_olustur()
#tablo_veri_ekleme('Adam','Smith', 19,'Male','Yönetici', 4400)
tablo_veri_cek() 
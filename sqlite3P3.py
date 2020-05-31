"""
imlec = cursor
baglanti = connect
"""

import sqlite3 
baglanti = sqlite3.connect("market.db")
imlec = baglanti.cursor()

def tablo_olustur():
    imlec.execute("create table if not exists products (p_Name TEXT,brand TEXT,price INT,piece INT)")
    baglanti.commit()
def tablo_veri_ekle(p_Name,brand,price,piece):
    imlec.execute("insert into products values(?,?,?,?)",(p_Name,brand,price,piece))
    baglanti.commit()
def tablo_veri_cek():
    imlec.execute("select * from products")
    veriler = imlec.fetchall()
    for i in veriler:
        print(i)
def tablo_veri_guncelle(old_name,new_name):
     imlec.execute("update Products set p_Name = ? where p_Name = ?",(new_name,old_name))
     baglanti.commit()
def tablo_veri_sil(p_Name):
    imlec.execute("delete from Products where p_Name =?",(p_Name,))  
    baglanti.commit()
tablo_olustur()
tablo_veri_guncelle("Kıvırcık Makarna", "Burgu Makarna")
tablo_veri_sil("xXx")
tablo_veri_cek()

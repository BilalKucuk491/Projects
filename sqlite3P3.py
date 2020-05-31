import sqlite3 
baglanti = sqlite3.connect("market.db")
imlec = baglanti.cursor()

def tablo_olustur():
    imlec.execute("create table if not exists urunler (urunAd TEXT,marka TEXT,fiyat INT,adet INT)")
    baglanti.commit()
def tablo_veri_ekle(urunAd,marka,fiyat,adet):
    imlec.execute("insert into urunler values(?,?,?,?)",(urunAd,marka,fiyat,adet))
    baglanti.commit()
def tablo_veri_cek():
    imlec.execute("select * from urunler")
    veriler = imlec.fetchall()
    for i in veriler:
        print(i)
def tablo_veri_guncelle(old_name,new_name):
     imlec.execute("update Urunler set urunAd = ? where urunAd = ?",(new_name,old_name))
     baglanti.commit()
def tablo_veri_sil(urunAd):
    imlec.execute("delete from Urunler where urunAd =?",(urunAd,))  
    baglanti.commit()
tablo_olustur()
tablo_veri_guncelle("Kıvırcık Makarna", "Burgu Makarna")
tablo_veri_sil("xXx")
tablo_veri_cek()
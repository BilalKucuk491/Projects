# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:38:37 2020

@author: BİLAL

imlec = cursor
baglanti = connect

"""


import sqlite3
baglanti = sqlite3.connect("company.db")
imlec = baglanti.cursor()

def create_table():
    imlec.execute("create table if not exists personels (name TEXT,lastname TEXT, age INT,gender TEXT,position TEXT, salary INT)")
    baglanti.commit()
    
def add_data(name,lastname,age,gender,position,salary):
    imlec.execute("insert into personels values (?,?,?,?,?,?)",(name,lastname,age,gender,position,salary)) 
    baglanti.commit()

def tablo_all():
    imlec.execute("select * from personels")
    datas = imlec.fetchall()
    for i in data:
        print(i)

create_table()
#add_data('Adam','Smith', 19,'Male','Engineer', 4400)
table_all() 

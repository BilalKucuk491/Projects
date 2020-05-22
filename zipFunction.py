# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:11:30 2020

@author: BİLAL
"""
from functools import reduce

a = reduce(lambda x,y : (x+y)**3,[1,2,3])
print(a)

tr_meyve = ["Elma","Muz","Çilek","Üzüm"]
eng_fruit = ["Apple"]
print(list(zip(eng_fruit,tr_meyve)))
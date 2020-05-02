# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:37:15 2020

@author: BİLAL
"""

class worker:
   def __init__ (self,salary,name,lastname,ethnicity,age,status):
        self.salary = salary
        self.name = name
        self.lastname = lastname
        self.ethnicity = ethnicity
        self.age = age
        self.status = status
        
   def ShowOn(self):
       print("""
       ------- Worker -----------------
       
       Name =  {}
       Lastname = {}
       Age = {}
       Ethnicity = {}
       Salary (Dolar) = {}
       Stattus = {}       
       
       ---------------------------------
       """.format(self.name,self.lastname,self.age,self.ethnicity,self.salary,self.status))

worker1 = worker(300,"Bilal","Kucuk","Asian","19","He is tired and angry.")
worker1.ShowOn()       
       
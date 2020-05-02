# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:37:15 2020

@author: BİLAL
"""

class worker:
   def __init__ (self,name,lastname,salary):
        self.salary = salary
        self.name = name
        self.lastname = lastname
        
   def ShowOn(self):
       print("""
       ------- Worker -----------------
       
       Name =  {}
       Lastname = {}
       Salary (Dolar) = {}     
       
       ---------------------------------
       """.format(self.name,self.lastname,self.salary))
       
class admin(worker):
    def __init__(self,name,salary,lastname,status):
        super().__init__(name,salary,lastname)
        self.status = status
        
    def Salary_Update(self,salary):
        self.salary = salary
    
    def ShowOn(self):
        print("Name = {}\nLastName = {} \nSalary = {} \nStattus = {}".format(self.name,self.lastname,self.salary,self.status))
              
       
admin1 = admin("Adrian","Eudoxus",1200,"He is tired")
admin1.ShowOn()
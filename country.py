# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:55:16 2020

@author: BİLAL

Hi guys, lets examples a oop.
Can you try the codes on your computer?
"""


class country():
    def __init__(self,countryName,population,Governmant,Languange,Religion):
        print("+"*25)
        self.countryname = countryName
        self.population= population
        self.governmant = Governmant
        self.languange = Languange
        self.religion = Religion
    def capital(self):#Since things like __x__ work when calling class, it wants us to assign at least 1 value to it.
         return "Angora"
    def __str__(self):
         print("Country:    {} \nGovernmant: {} \nLanguage:   {}\nReligion:   {} ".format(self.countryname,self.governmant,self.languange,self.religion))
    def __len__(self):
        return self.population
turkey = country("Turkey","95 million","Republic","Turkish","Seculer")
turkey.__str__()
print("Population:",turkey.__len__())

print("Capital:   ",turkey.capital())
print("+"*25)

print(len(turkey.population)
del turkey
#print(turkey.capital()) Name 'turkey' is not defined.

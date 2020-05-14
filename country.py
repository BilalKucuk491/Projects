# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:55:16 2020

@author: BİLAL
"""


class country():
    def __init__(self,countryName,population,Governmant,Languange,Religion):
        print("+"*25)
        self.countryname = countryName
        self.population= population
        self.governmant = Governmant
        self.languange = Languange
        self.religion = Religion
    def capital(self):# __x__ gibi şeyler class çağırıldında çalıştığığ için içine en az 1 tane değer atamamızı ister
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

print(len(turkey.population))# __len__() ile len() fonksiyonu(methodu) arasındaki fark len fpnksiyonu kapladığı bit kadar yeri sayar __len__() ise farklı uzunlukları tanımlayıp onları kullanmaktır.
del turkey
#print(turkey.capital()) Name 'turkey' is not defined.

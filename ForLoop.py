# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:53:54 2020

@author: BİLAL

y =["Ali",1,12.4,"Elma",False]
a = False in y
print(a)

liste = [1,2,3,4,5]
for a in liste:
    print(a)
    
teste = ("John",12.5,15,True)
for x in teste:
    print(x)    

teste = int(input("Enter a number: "))
summ = 
for x in teste:
    summ += x
print(summ)    

print("Factorial Calculator")
number = (1,2,3,4,5,6,7,8,9)
fac = 1
for x in number:
    fac = x*fac
print("{}! = {}".format(number,fac))

teste = (1,2,3,4,5,6,7,8,9,10)
summ = 0
for x in teste:
    if x %2 == 1:
        summ +=x
print(summ)   

numbers = [(1,5),(2,6),(3,7),(4,8)]
for x,y in numbers:
    print(x,y) 

dictionary = {"Apple": "Elma","Computer":"Bilgisayar","Tree":"Ağaç","Chocolate":"Çikolata"}
for a in dictionary.keys():
    print(a)
"""   
numbers = range(0,100)
summ = 0
for x in numbers:
    summ +=x
print(summ) 
a = (100*99)/2
print(a)   

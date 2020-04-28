# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:42:03 2020

@author: BİLAL


c = 110
def carpma(a,b):
    global c
    return a*b + c

print(carpma(2,3))

number_mod = lambda num1,num2: num1 % num2
print(number_mod(9, 2)) 

kuvvetAl =lambda taban,kuvvet: taban**kuvvet
print(kuvvetAl(2, 4))


x = int(input("Enter a number "))

odd_or_even = lambda x : x % 2 == 0 

if odd_or_even(x):
    print("Even")
else:
    print("Odd")

num = int(input("Enter a number: "))
def integer_divisor (num):
    liste = list()
    for i in range(1,num+1):
        if  num % i ==0:
            liste.append(i)
    return liste
print(integer_divisor(num))        

num = int(input("Enter a number: "))
def prime_number(num):
    if num %2 != 0 or num %3 != 0 or num == 2:
        print("Prime Number")
    else:
        print("Not Prime Number")

print(prime_number(num))

def prime_number(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True

while True:
    num = int(input("Enter a number "))
    if prime_number(num):
        print("This is prime number.")
    else:
        print("This is not prime number.")
    exitt = input("'q' for exit or enter.  ")
    if exitt == "q":
        break

def ebob(num1,num2):
    big_num = max(num1,num2)
    sm_num = min (num1,num2)
    liste = list()
    for i in range(1,big_num*sm_num+1,1):
        if num1 % i == 0 and num2 % i == 0 :
              liste.append(i)
    liste.sort(reverse=True)          
    return  liste
   
print(ebob(30,20))    
"""
num1 = int(input("Number one: "))
num2 = int(input("Number two: "))

def ekok(num1,num2):
    liste=list()
    for i in range( max(num1,num2) , num1*num2 + 1):
        if i % num1 == 0 and i % num2 == 0:
            liste.append(i)
    return liste[0]

print("Bu sayıların ekoku: ", ekok(num1,num2 ))      

        

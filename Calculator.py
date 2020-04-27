# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:32:30 2020

@author: BİLAL
"""
print("""
Options;
[0] +
[1] -
[2] *
[3] /
[4] Exit

Please enter the larger number in the 1st issue..
    """)

secim = float(input("You are selection:  "))
num1 = float(input("Number one: "))
num2 = float(input("Number two: "))
if secim == 0 : 
    print("\n + : {}".format(num1+num2))
elif secim == 1:
    print("\n - : {}".format(num1-num2))
elif secim == 2: 
    print("\n * : {}".format(num1*num2))
elif secim == 3:
    print("\n / : {}".format(num1/num2))
elif secim == 4:
    print("You are exit")
else:
    print("Hi,This is console calculator")
        

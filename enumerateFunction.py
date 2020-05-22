# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:59:29 2020

@author: BİLAL
"""


a = list(enumerate(["Math","English","Chemistry","Biology","Physics","History","Geography",False,12.2,1,-1]))
t = 0
for i in a:
    print("{}.index : {}".format(t,i))
    t +=1

print(type(False),type(1),type("physics"),type(1.2)) 
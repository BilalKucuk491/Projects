# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:26:28 2020

@author: BİLAL
"""

class vegan:
    def __init__ (self,bieber,lime,cucumber,onion):
        print("*"*24)
        self.bieber = bieber
        self.lime = lime
        self.cucumber = cucumber
        self.onion = onion
    def ShowOn(self):
      print(" Bieber price: {} \n Lime price : {} \n Cucumber price : {} \n Onion price : {}\n".format(self.bieber,self.lime,self.cucumber,self.onion))
      print("*"*24)
    
basket1 = vegan("2.5$","5$","2$","3$")
basket1.ShowOn()


# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 17:06:35 2020

@author: BİLAL
"""

BookList = ["Pinocchio","Atatürk","The upon time Anatolia","Hugo","War and Peace","Alice in Wonderland"]
menu = """

[0] Add book
[1] Take out a book
[2] list books
[Q] Quit

"""

def AddBook(book,liste):
    liste += [book]
    print("Book added! ")
    input("Enter for menu")

    
def DeleteBook():
    pass

def Listele(liste):
    for i in liste:
        print("Book name =====>  {}".format(i))
    input("Enter for menu")
    
    
while True:
    print(menu)
    secim = input("You are selection: ")
    
    if secim == "0":
        BookName = input("Book Name: ")
        AddBook(BookName, BookList)
        
    elif  secim == "1":
        DeleteBook()
        
    elif secim == "2":
        Listele(BookList)
        
    elif secim == "q" or secim == "Q":
        quit()
        
    else:
        print("Error 404")
        input("Enter for menu")
        
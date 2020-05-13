# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:20:51 2020

@author: BİLAL
This is code bloks for you free
I hope, you will succesfull.
"""
import time as timee
import random as randomm


class musicPlayer():
    def __init__(self,songs=[]):
        self.songs = songs
        self.status = True
        self.sound = 100
        self.playSong = ""
        
    def soundBoost(self):
        if(self.sound > 95):
            pass
        else:
            print("Sound boost.")
            timee.sleep(2)
            print("Sound boost. Sound : {}".format(self.sound))
            self.sound +=5
            
    def soundReduction(self):
        if (self.sound < 0):
            self.sound = 0
        else:
            self.sound -=5
            timee.sleep(2)
            print("Sound reduction . Sound : {}".format(self.sound))
            
    def addSong(self,song):
        self.songs.append(song)
    
    def songList(self):
        print(self.songs)
        return self.songs
    
    def songSel(self):
        count = 1
        for i in self.songs:
            print("{}.{}".format(count,i))
            count += 1
            selection = int(input("Select song number : "))
            print("Changed song.")
            timee.sleep(2)
            self.playSong = self.songs[selection-1]
            print("Changed a song, song right now : {}".format(self.playSong))
            
    def randomSel(self):
        random_num = randomm.randint(0, len(self.songs))
        self.playSong = self.songs[random_num]
        
    def close(self):
        self.status = False
        
    def deleteMusic(self):
        count = 1
        for i in self.songs:
            print("{}.{}".format(count,i))
            count += 1
        selection = int(input("Please, enter a delete song number"))    
        self.songs.pop(selection-1)
    
    def interface(self):
        print("""
              
              Song list = {}
              Song = {}
              Sound = {}
              Status = {}
        
                
              1-Select song
              2-Sound increase
              3-Sound reduction
              4-Select random song
              5-Add song
              6-Delete song
              7-Close""".format(self.songs,self.playSong,self.sound,self.status))
            
p1 = musicPlayer(songs = ["Bts - DNA"])

while p1.status == True:
    
    p1.interface()
    selection = int(input("Enter the number you chose : "))
    
    if (selection == 1):
        p1.songSel()
        
    elif (selection == 2):
        p1.soundBoost()
        
    elif (selection == 3):
        p1.soundReduction()
        
    elif (selection == 4):
        p1.randomSel()
        
    elif (selection == 5 ):
        song = input("Enter a song : ")
        p1.addSong(song)
        
    elif (selection == 6):
        p1.deleteMusic()
        
    else:
        p1.close()
    
    
        

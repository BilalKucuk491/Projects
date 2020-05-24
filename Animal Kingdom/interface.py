from life import invertebrates,vertebrates

def interFace():
    
    while True:
        
        print("""
                  
             1)Read
             2)Write
             0)Exit
       """)
        v = int(input("Select a number : "))
        if v == 1:
            
            print("""
                      
            1)Invertebrates
            2)Vertebrates
            0)Exit
            """)
                
            v1 = int(input("You are selection : "))
            if v1 == 1: 
                
                print("""      
                1)Sponges
                2)Solent
                3)Worms
                4)Molluscs
                5)Arthropod
                6)Echinoderm
                    
                exit = 0
                """)
                v2 = int(input("You are selection : "))
                if v2 == 1:
                    invertebrates.sponges()
                elif v2 ==2:
                    invertebrates.solent()
                elif v2 == 3:
                    invertebrates.worms()
                elif v2 == 4:
                    invertebrates.molluscs()  
                elif v2 == 5:
                    invertebrates.arthropod()
                elif v2 == 6:
                    invertebrates.echinoderm() 
                else:
                    break
            if v1 == 2: 
                
                print("""      
                1)Fishes
                2)Two-Living
                3)Reptiles
                4)Birds
                5)Mammals
                    
                exit = 0
                """)
                v2 = int(input("You are selection : "))
                if v2 == 1:
                    vertebrates.fishes()
                elif v2 ==2:
                    vertebrates.two_Living()
                elif v2 == 3:
                    vertebrates.reptiles()
                elif v2 == 4:
                    vertebrates.birds  
                elif v2 == 5:
                    vertebrates.mammals()
                else:
                    break   
        elif v == 2:
            pass
        else:
            break
    
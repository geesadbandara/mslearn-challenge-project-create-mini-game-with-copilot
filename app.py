
import random


def compGen():
    genVal = random.randint(1,3)
    print(genVal)
    if(genVal == 1):
        genSelect = "rock"
    elif(genVal==2):
        genSelect = "paper"
    else:
        genSelect = "scissor"
    return genSelect

def checkUser(genSelect, userSelect):
    if(genSelect=="rock" and userSelect == "scissor"): 
        print("Lost")
    elif(genSelect=="scissor" and userSelect == "rock"):
        print("Won")

    #create same structure for scissor and paper   
    elif(genSelect=="paper" and userSelect == "scissor"): 
        print("Won")
    elif(genSelect=="scissor" and userSelect == "paper"):
        print("Lost")
    
    elif(genSelect=="rock" and userSelect == "paper"): 
        print("Won")
    elif(genSelect=="paper" and userSelect == "rock"):
        print("Lost")
    
    else:
        print("Draw")

while(True):
    userSelect = input("Enter rock, paper or scissor: ")
    genSelect = compGen()
    checkUser(genSelect, userSelect)
    playAgain = input("Do you want to play again? (y/n): ")
    if(playAgain == "n"):
        break


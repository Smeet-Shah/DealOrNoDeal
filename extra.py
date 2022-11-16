'''
Title: Extra Module
Description: Contians the functions that are not directly part of the game but "make it better"
Created By: Smeet Shah
Date Created: 06/06/22
Date Last Modified: 19/06/22
'''

# Imports
import os, time


# Clears console
# Inspired from Delftstack
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)


# Takes in users game name for future purposes
def playerIntro():
    userName = input("Please enter your name: ") 
    return userName


# Displays Previous Scores
def displayScore(scoreFile):
    clear()
    inFile = open ("previousWinners.txt", "r")
    for i in range (7): 
        print (inFile.readline().strip())
    input("To continue please enter 1:\n>>> ")
    clear()
    return False


# Adds new scores in recent score file
def pastScore (userName, score): 

    scoreFile = open("previousWinners.txt","r") 
    oldScore = (userName +": $"+ str(score)+"\n")      
    newScore = scoreFile.readlines()  
    newScore.insert(2, oldScore) 
    scoreFile.close() 
 

    scoreFile = open ("previousWinners.txt","w") 
    scoreFile.writelines(newScore) 
    scoreFile.close()


# Opens case slowly
def displayValueCase(value, case):
    clear()
    print("Opening case in 3...")
    time.sleep(0.5)
    print("Opening case in 2...")
    time.sleep(0.5)
    print("Opening case in 1...")
    time.sleep(0.5)
    print("|", case, "| contained: $" + str(value))
    input("Press enter to continue")
    clear()

# Displays the first chosen case 
def chosenCase(caseNum):
    clear()
    print("You've chosen the following case:")
    print("|", caseNum, "|")
    input("Press enter to continue")
    clear()
   
# Prints text slower
# Credits to W3Schools
def print_slow(txt):
    for x in txt:  
        print(x, end='', flush=True)
        time.sleep(0.1)
    print()

ascii = {"Intro":"""

 ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄                 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄           
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌               ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░▌      ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌               ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌          
▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌               ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌          
▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌               ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌          
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌               ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          
▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌               ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀      ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌          
▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌               ▐░▌       ▐░▌▐░▌     ▐░▌       ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌      ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌      ▐░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀       ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                                                                                                                              
Select an option:
    A) Play
    B) Instructions
    C) Show Previous Winners
    D) Quit

>>> """, "Ending":"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠶⠶⠶⠀⠀⠸⠏⠉⠉⠉⠉⠹⠇⠀⠀⠶⠶⠶⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣶⣶⠀⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠀⣶⣶⣄⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠙⠿⠿⠀⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠿⠿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""}

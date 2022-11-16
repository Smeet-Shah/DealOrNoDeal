'''
Title: Menu Module
Description: Contians the functions that relate to the Introduction Menu
Created By: Smeet Shah
Date Created: 06/06/22
Date Last Modified: 19/06/22
'''

# Imports
import sys, random, os, extra


# Beginning Menu 
def on():
    choice = input(extra.ascii["Intro"])

    if choice.lower() == "a":
        openMenu = False
        highScore = False
    if choice.lower() == "b":
        openMenu = instructions()
        highScore = False
    if choice.lower() == "c":
        openMenu = True
        highScore = True
    if choice.lower() == "d":
        extra.clear()
        print(extra.ascii["Ending"])
        sys.exit("Let's make a deal... next time!")
    return openMenu, highScore
    
    
# Displays instructions
def instructions():
    extra.clear()
    print('''
Instructions // How to play:

- There are 26 briefcases all with a value ranging from $0.01 to $1,000,000

- You will choose 1 case from the 26 and it's value will be kept hidden til the end of the game

- You will then choose cases to remove from the remaining left. Each case you remove will also remove the money from the board.

- After a number of cases removed, the Banker will give you an offer based off how much money is on the board and the chances of you going home with a lot money

- You will either say DEAL or NO DEAL

- You're goal is to go home with the most money you can
    ''')
    input("To exit please press enter\n>>> ")
    extra.clear()
    openMenu = True
    return openMenu


# Displays the Final Menu
def finalMenu(name, amount, count):
    newAmount = amount
    if count == 0:
        extra.pastScore(name, newAmount)
        count = 1
    extra.clear()
    choice = input("""
Thank you for playing Deal or No Deal!

Select an option:
    A) Play again
    B) Recent Scores
    C) Quit

>>> """)

    if choice.lower() == "a":
        rePlay = True
        openMenu = True
        showScore = False
        showEnd = False
    if choice.lower() == "b":
        rePlay = True
        openMenu = True
        showScore = True
        showEnd = True
    if choice.lower() == "c":
        extra.clear(        )
        print(extra.ascii["Ending"])
        sys.exit("Let's make a deal... next time!")

    return rePlay, openMenu, showScore, showEnd, count


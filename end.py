'''
Title: End Module
Description: Contians the function that are run in the final menu to avoid confusion with the Menu module and it's functions
Created By: Smeet Shah
Date Created: 06/06/22
Date Last Modified: 19/06/22
'''

# Imports
import extra, game, menu, sys

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


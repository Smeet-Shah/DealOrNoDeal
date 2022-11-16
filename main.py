'''
Title: The Last Dance // DEAL OR NO DEAL
Description: Game runs Deal or No Deal with slightly modified rules.
Created By: Smeet Shah
Date Created: 06/06/22
Date Last Modified: 19/06/22
'''

# Imports
import menu, game, extra, end

# Variables to Start Game
openMenu = True
rePlay = True

# Name for Scores
name = extra.playerIntro()

# Loop to play/replay game
while rePlay:
    showEnd = True
    scoreCounter = 0

# Loop to open menu or show highscores
    while openMenu:
        openMenu, highShow = menu.on()

        if highShow:
            openMenu = True
            highShow = extra.displayScore ("previousWinners.txt")
     
# Game Intiation
    amount = game.main()

# Loop to display End Menu
    while showEnd:
        rePlay, openMenu, highShow, showEnd, scoreCounter = menu.finalMenu(name, amount, scoreCounter)
                    
        if highShow:
            highShow = extra.displayScore("previousWinners.txt")
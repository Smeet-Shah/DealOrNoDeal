'''
Title: Game Module
Description: Contians the functions that run the game itself
Created By: Smeet Shah
Date Created: 06/06/22
Date Last Modified: 19/06/22
'''

# Imports
import random, sys, end, menu, extra, time

# The function the game runs through // All other game functions are called here
def main():

    # Globalizes the variables and resets each time after the game is run
    global cases, valueRemain, casesRemain, selectedCases, valueCase
    cases, valueRemain, casesRemain, selectedCases, valueCase = reset()

    displayBoard()
    firstCase = input("Choose your case (Enter a number between 1 and 26): ")

    if int(firstCase) < 1 or int(firstCase) > 26:
        print ("Enter a valid case!")
        main()

    else:
        extra.chosenCase(firstCase)                     # Prints the case chosen to the user
        tempCase = random.choice(cases)                 # Assigns first case value chosen to variable
        cases.remove(tempCase)                          # Removes first case's value from available
        valueCase.append(tempCase)                      # Appends First Case to list
        selectedCases.append(firstCase)                 # Appends Case Number into list of chosen cases

        amount = removeCase(firstCase, selectedCases)   # Runs next part of game
        return amount
        
# Runs the removing cases portion of the game // Asks the user for a case to remove
def removeCase(firstCase, selectedCases):
    turn = 3

    while turn != 0:
        displayBoard()
        cutCase = input("Choose a case to remove (Enter a number between 1 and 26): ")

        if int(cutCase) < 1 or int(cutCase) > 26:
            print ("Enter a valid case")
            input("Press enter to continue >>>")
            continue

        if cutCase in selectedCases:
            print ("Enter a case that has not be chosen")
            input("Press enter to continue >>>")
            continue
        else:
            casesRemain.remove(int(cutCase))            # Removes case number chosen from display
            tempCase = random.choice(cases)             # Assigns chosen case's value
            valueRemain.remove(tempCase)                # Removes case number's value from display
            
            extra.displayValueCase(tempCase, cutCase)   

            cases.remove(tempCase)                      # Appends Case Number into list of chosen cases
            selectedCases.append(cutCase)

            turn = turn - 1

    amount = bankerOffer(firstCase, selectedCases)      # Runs the next part of the game // Banker
    return amount

# Determines banker offer and runs the choices when the offer is represented
def bankerOffer(firstCase, selectedCases):
    offer = round(0.8*(sum(cases)/float(len(cases))), 2)

    if len(cases) == 1:
        finalChoice = input("Would you like to keep your case? (Yes or No): ") 
        if finalChoice.lower() == "yes":
            finalCase = sum(valueCase)
            print ("You won $", finalCase)
            print("The other case contained $" + str(cases[0]))
            input("Press enter to continue >>>")
            return finalCase
            
        
        elif finalChoice.lower() == "no":
            print ("You won $" + str(cases[0]))
            finalCase = sum(valueCase)

            print ("Your case contained $" + str(finalCase))
            input("Press enter to continue >>>")
            return offer
            

        else:
            print ("Yes or No? Please pick one or the other.")
            bankerOffer(firstCase, selectedCases)

    if len(cases) > 1:
        
        offerLoad(offer)
        finalChoice = input("")

        if finalChoice.lower() == "yes":
            extra.clear()
            print ("You've won $" + str(offer))
            finalCase = sum(valueCase)

            print ("Your case contained $" + str(finalCase))
            input("Press enter to continue >>>")
            return offer


        elif finalChoice.lower() == "no":
            amount = removeCase(firstCase, selectedCases)
            return amount

        else:
            print ("Yes or No? Please pick one or the other.")
            bankerOffer(firstCase, selectedCases)

# Displays the cases and amount of money on the board
def displayBoard():
    extra.clear()
    print ("Here is the money on the board:")
    for i in range(len(valueRemain)):
        if i % 4 == 0:
            print("")
            print("$" + str(valueRemain[i]), end = "   ")
        else:
            print ("$" + str(valueRemain[i]), end = "   ")

    print("")
    print("")

    print ("Here are the cases on the board:")
    for i in casesRemain:
        if i % 4 == 0:
            print("|",i,"|", end = "    ")
            print("")
        else:
            print("|",i,"|", end = "    ")
    print("")
    print("")

# Key lists and values are reseted for a new game
def reset():
    cases = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750,1000, 5000, 10000, 25000, 50000, 75000,100000, 200000,300000, 400000, 500000, 750000, 1000000]
    valueRemain = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750,1000, 5000, 10000, 25000, 50000, 75000,100000, 200000,300000, 400000, 500000, 750000, 1000000]
    casesRemain = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

    selectedCases = []
    valueCase = []
    return cases, valueRemain, casesRemain, selectedCases, valueCase

# Slow prints the bankers offer
def offerLoad(offer):
    extra.print_slow("The Banker is making his offer...")
    print ("The Banker has offered $" + str(offer), "Do you accept, Yes or No? ")


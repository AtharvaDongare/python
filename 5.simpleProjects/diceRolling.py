"""
input : 
    1. no. of dices
    2. min dice value
    3. max dice value

output :
    dices rolled to provide values
"""


import random

diceCount = 4
minDiceVal = 1
maxDiceVal = 10

def rollDices(diceCount, minDiceVal, maxDiceVal):
    diceList = []
    for dice in range(0,diceCount):
        diceVal = random.randint(minDiceVal, maxDiceVal)
        diceList.append(diceVal)
    return diceList

def getInput():
    option = str(input("enter \"roll\" to roll the dices\n: "))
    return

def main():
    option = getInput()
    while(option != "exit"):
        if option == "roll":
            diceValues = rollDices(diceCount, minDiceVal, maxDiceVal)
            print(">> ", diceValues)
            option = getInput()
        else:
            print(">> ", "invalid option")
            option = getInput()
    else:
        print(">> ", "thanks for playing")


if __name__ == "__main__":
    main()
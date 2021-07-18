"""
This program generates a random number between 1-100
and lets the user guess the number.
"""

import random

def main():
    solutionNumber = random.randint(1,100)
    # print(solutionNumber)
    gameEndFlag = False
    try:
        while not gameEndFlag:
            guessNumber = int (input("Guess the number : "))
            if guessNumber == solutionNumber:
                print("The guess is correct. Thanks for playing")
                gameEndFlag = True
            elif (guessNumber > solutionNumber):
                print("your guess is little too high")
            elif (guessNumber < solutionNumber):
                print("your guess is little too low")
    except ValueError:
        print("please enter correct value")

if __name__== "__main__":
    main()
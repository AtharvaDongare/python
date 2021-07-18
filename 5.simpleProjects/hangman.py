"""
guess the word

while not max attemp
    ask user to enter character
    print the word with character in place
    if char not in word, incr attempt count
        if max attempt reached, game over
"""

word = "LoremIpsumissimplydummytextoftheprintingandtypesettingindustry"

def getRandomWord():
    return word.lower()

def getWordChars(word):
    wordChars=[]
    for ch in word:
        if ch not in wordChars:
            wordChars.append(ch)
    return wordChars


def main():
    word = getRandomWord()
    wordChars = getWordChars(word)
    for w in word:
        if w in guessedChars:
            print(w, end=" ")
        else:
            print("_", end=" ")
    print("\n")
    # print(wordChars)


if __name__ == "__main__":
    main()

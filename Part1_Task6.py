import random

def getFileContents(fileName):
    with open(fileName,"r") as file:
        lines = list(map(lambda x:x.strip("\n"),file.readlines()))
    return lines

def getTiles():
    return getFileContents("tiles.txt")

def getDictionary():
    return getFileContents("dictionary.txt")

def onlyEnglishLetters(word):
    try:
        word = word.upper()
        for i in word:
            asc = ord(i)
            if asc > 90 or asc < 65:
                return  False
        return True
    except AttributeError:
        return False

def canBeMade(word, myTiles):
    for letter in word:
        if letter not in myTiles:
            return False
        else:
            myTiles.remove(letter)
    return True

def isValid(word,myTiles,dictionary):
    if onlyEnglishLetters(word) == False:
        return False
    elif canBeMade(word,myTiles) == True:
        return True
    elif word not in dictionary:
        return False
    else:
        return True


Tiles = getTiles()
dictionary = getDictionary()

listoftiles = []
for x in Tiles:
    x = x.split()
    listoftiles.append(x)

myTiles = []
for i in range(0, 7):
    myTiles += random.choice(listoftiles)
print(myTiles)

word = input("Enter a word: ")
print(isValid(word,myTiles,dictionary))


#Author Kevin Hann



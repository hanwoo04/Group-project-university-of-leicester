import random

def canBeMade(word, myTiles):
    for letter in word:
        if letter not in myTiles:
            return False
        else:
            myTiles.remove(letter)
    return True

Tiles = open("tiles.txt", "r")

listoftiles = []
for x in Tiles:
    x = x.split()
    listoftiles.append(x)
myTiles = []
for i in range(0, 7):
    myTiles += random.choice(listoftiles)
print(myTiles)

word = input("Enter the word: ")
print(canBeMade(word.upper(), myTiles))


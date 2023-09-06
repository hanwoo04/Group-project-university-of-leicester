import random

def getFileContents(fileName):
    with open(fileName,"r") as file:
        #removes \n from any lines that have them
        lines = list(map(lambda x:x.strip("\n"),file.readlines()))
    return lines


#gets the scores from the file and puts them into a dictionary
def getScores():
    lines = getFileContents("scores.txt")
    #adds all the scores to a adictionary and assigns them their scores
    dict = {}
    for i in lines:
        newLine = i.split(" ")
        dict[newLine[0]] = newLine[1]
    return dict

#returns the contents of tiles as a list
def getTiles():
    return getFileContents("tiles.txt")

#returns the dictionary as a list
def getDictionary():
    return getFileContents("dictionary.txt")

def onlyEnglishLetters(word):
    try:
        #converts the word into upper case to make the if statement simpler
        word = word.upper()
        for i in word:
            # checks if the ascii value of each character is within the range to be a valid character
            asc = ord(i)
            if asc > 90 or asc < 65:
                return  False
        return True
    #returns false if word is not a string
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
        print("Only use English letters")
        return False
    if canBeMade(word,myTiles) == False:
        print("Word cannot be made from these tiles")
        return False
    if word not in dictionary:
        print("There is no such word in the dictionary")
        return False
    return True

def getLetterScore(letter):

    try:
        scores = getScores()
        return int(scores[letter])
    except:
        return "Something went wrong"

def getWordScore(word):
    total_score = 0
 #   try:
    for letter in word:
        total_score += getLetterScore(letter.upper())

    invalid = any(letter.isdigit() for letter in word)
    if invalid:
        return "Invalid word"
    else:
        return "Word score is: " + str(total_score)
   # except TypeError:
  #      return "Invalid character, use numbers only"
Scores = getScores()
Tiles = getTiles()
Dictionary = getDictionary()
myTiles = []
for i in range(0, 7):
    myTiles += random.choice(Tiles)
myScores = list(map(lambda x: Scores[x],myTiles))


#Formats the display 
str_tiles = ""
str_scores = ""
for let in myTiles:
    str_tiles += str(let) + " "

for let in myScores:
    str_scores += str(let) + " "

print("Generating random tiles...")
print(f"Tiles: {str_tiles}")
print(f"Scores: {str_scores}")


start = True
while start:
    userInput = input("Enter a word: ").upper()
    if userInput == "&&&":
        print("Thanks for using this application, better luck next time!!!")
        start = False
    else:
        if isValid(userInput,list(myTiles),Dictionary) == False: #myTiles is cast to list to avoid pass by reference bugs
            continue
        else:
            print("You got it right, this is a valid word")
            print(f"Score of this word is: {getWordScore(userInput)}")


# Test No   Test Desc                  Expected outcome               Actual outcome               Fix
# 1         user enters &&&            application closes             Expected
# 2         user enters a valid word   application outputs score      Expected
# 3         User enters a word not     Application tells the user the Expected
#           in the dictionary          word is not in the dictionary    
# 4         User enters a word that    Application tells the user the Expected
#           cant be made from the      word cant be made
#           tiles    
# 5         User enters a non english   Application tells the user to Expected
#           character                   user only english letters
#          
# 6         User enters the same       Application prints out the     Second output is word cant   casted the tiles to a list
#           valid word twice in a row  scores for the word twice      be made using tiles 
# 
# 7         User enters a word using   Application says the word 
#           the same letter twice      cant be made                   Expected
#           (the tile only appears once)
#       

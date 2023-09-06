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

Scores = getScores()
Tiles = getTiles()
Dictionary = getDictionary()
print(Scores)
print(Tiles)
print(Dictionary)

#Author Sam Green

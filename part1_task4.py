from part1_task3 import getLetterScore


def getWordScore(word):
    total_score = 0
    try:
        for letter in word:
            total_score += getLetterScore(letter.upper())

        invalid = any(letter.isdigit() for letter in word)
        if invalid:
            return "Invalid word"
        else:
            return "Word score is: " + str(total_score)
    except TypeError:
        return "Invalid character, use numbers only"


#               Test Script
#Input          Expected output         Actual Output
#a              Word score is: 1         Word score is: 1
#apple          Word score is: 15        Word score is: 15
#"3"            Invalid character, use numbers only  Invalid word
#3              Invalid character, use numbers only  Invalid character, use numbers only
#3hundred       Invalid word             Invalid word


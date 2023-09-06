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

print(onlyEnglishLetters("Z"))

#Author Sam Green
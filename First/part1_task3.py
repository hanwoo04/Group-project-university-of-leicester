def getLetterScore(letter):

    try:
        score_list = []
        scores = open("scores(1).txt", "r")
        for line in scores:
            line = line.strip().split(" ")
            score_list.append(line)
        if len(letter) > 1:
            return "Error! Use only one letter"

        for i in range(len(score_list)):
            for j in range(1):
                if letter.upper() == score_list[i][0]:
                    return int(score_list[i][1])
        if letter.upper() not in score_list:
            return 0

    except FileNotFoundError:
        return "File not found"

    except:
        return "Something went wrong"


#               Test Script
#Input          Expected output         Actual Output
#a              1                       1
#j              10                      10
#"3"             0                      0
#3          "Something went wrong"      "Something went wrong"
#aj    "Error! Use only one letter"    "Error! Use only one letter"

#Author Isiah Jones

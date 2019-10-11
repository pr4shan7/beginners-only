# Magic8-Ball, run this script to get a prediction
import random   #using random module to get random predictions
def getpredict(answerNumber):
    if answerNumber == 1:
        return "It is certain."
    elif answerNumber == 2:
        return "My sources say no."
    elif answerNumber == 3:
        return "It is decidedly so."
    elif answerNumber == 4:
        return "Reply hazy try again."
    elif answerNumber == 5:
        return "Outlook not so good."
    elif answerNumber == 6:
        return "Concentrate and ask again."
    elif answerNumber == 7:
        return "My reply is no."
    elif answerNumber == 8:
        return "Ask again later."
print(getpredict(random.randint(1, 8)))

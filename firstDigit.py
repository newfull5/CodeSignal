def firstDigit(inputString):
    for i in range(0,len(inputString)):
        if inputString[i].isnumeric():
            return inputString[i]

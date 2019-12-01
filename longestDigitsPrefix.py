def longestDigitsPrefix(inputString):
    for i in range(0, len(inputString)):
        if not inputString[i].isnumeric():
            return inputString[:i]
        
    return inputString

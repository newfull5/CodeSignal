def checkPalindrome(inputString):
    i=0
    j=len(inputString)-1
    
    while i <= len(inputString):
        if inputString[i] == inputString[j]:
            i =+ 1
            j =- 1
        else:
            return false
    return true

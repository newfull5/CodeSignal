def palindromeRearranging(inputString):
    for i in range(0,len(inputString)):
        for j in range(i+1,len(inputString)):
            if inputString[i] == inputString[j] and inputString[i] != '0':
                inputString = inputString.replace(inputString[i],'0',1)
                inputString = inputString.replace(inputString[j],'0',1)

    inputString = inputString.replace('0','')

    if len(inputString) == 1 or len(inputString) == 0:
        return True
    else:
        return 1==2

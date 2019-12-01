def isBeautifulString(inputString):
    inputString = list(inputString)
    inputString.sort()
    k = []
    for i in range(97, ord(inputString[-1])+1):
        k.append(inputString.count(chr(i)))
    if 0 in k:
        return False
    for i in range(0,len(k)-1):
        if k[i] < k[i+1]:
            return False
    return True

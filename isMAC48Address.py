def isMAC48Address(inputString):
    if len(inputString) != 17:
        return False
    
    inputString = inputString.replace('-','')
    
    if len(inputString) != 12:
        return False
    
    for i in range(0,len(inputString)):
        if inputString[i].isnumeric() or 65<=ord(inputString[i])<=70:
            continue
        else:
            return False
        
    return True

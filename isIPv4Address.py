def isIPv4Address(inputString):
    inputString = inputString.split('.')

    if len(inputString) != 4:
        return False
    
    for num in inputString:
        if not num.isnumeric():
            return False

    for num in inputString:
        if int(num) < 0 or int(num) > 255:
            return False

    return True

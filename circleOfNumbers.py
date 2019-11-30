def circleOfNumbers(n, firstNumber):
    if firstNumber >= n//2:
        return firstNumber-(n//2)
    else:
        return (n//2)+firstNumber

def squareDigitsSequence(a0):
    prev = []
    prev.append(a0)
    
    while True:
        lists = list(str(a0))
        sums = 0
        for num in lists:
            sums += int(num)**2
        if sums in prev:
            break
        prev.append(sums)
        a0 = sums
        
    return len(prev)+1

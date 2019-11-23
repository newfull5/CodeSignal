def isLucky(n):
    n = str(n)
    fir = []
    sec = []
    
    for i in range(0, len(n)//2):
        fir.append(int(n[i]))

    for i in range(len(n)//2, len(n)):
        sec.append(int(n[i]))
        
    return sum(fir) == sum(sec)

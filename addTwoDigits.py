import re

def addTwoDigits(n):
    p = re.compile('\d')
    n = str(n)
    k = p.findall(n)
    k = map(int, k)
    
    return sum(k)

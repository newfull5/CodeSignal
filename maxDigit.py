import re

def maxDigit(n):
    n = str(n)
    m = re.compile('\d')
    k = m.findall(n)
    return int(max(k))
    

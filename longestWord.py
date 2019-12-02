import re

def longestWord(text):
    p = re.compile('[a-zA-Z]+')
    result = p.findall(text)
    k = []
    for word in result:
        k.append(len(word))
        
    return result[k.index(max(k))]

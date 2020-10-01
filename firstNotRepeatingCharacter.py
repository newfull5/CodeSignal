def firstNotRepeatingCharacter(s):
    answer = "_"
    dic = {}
    for i,c in enumerate(s):
        if c in dic:
            dic[c] = -1
        else:
            dic[c] = i
    min_ = float('inf')

    for c in dic:
        if dic[c] > -1:
            return c
            
    return answer

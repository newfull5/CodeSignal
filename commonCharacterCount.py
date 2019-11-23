def commonCharacterCount(s1, s2):
    cnt = 0
    
    for i in range(0, len(s1)):
        for j in range(0, len(s2)):
            if s1[i] == s2[j]:
                s2 = s2.replace(s2[j], '', 1)
                cnt += 1
                break
                
    return cnt

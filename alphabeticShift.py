def alphabeticShift(inputString):
    answer = ''
    for word in inputString:
        answer += chr(ord(word)+1)
    answer = answer.replace('{','a')
    
    return answer

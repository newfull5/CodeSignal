def allLongestStrings(inputArray):
    word = 0
    answer = []
    
    for arr in inputArray:
        if word <= len(arr):
            word = len(arr)

    for arr in inputArray:
        if len(arr) == word:
            answer.append(arr)
            
            
    return answer

def addBorder(picture):
    answer = []
    sol = []
    
    for num in picture:
        answer.append('*'+num+'*')
        
    sol.append('*'*len(answer[0]))
    
    for num in answer:
        sol.append(num)
        
    sol.append('*'*len(answer[0]))
    
    return sol

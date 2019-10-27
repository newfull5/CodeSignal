def makeArrayConsecutive2(statues):
    answer = []
    
    for i in range(min(statues), max(statues)):
        if i not in statues:
            statues.append(i)
            answer.append(i)
            
    return len(answer)

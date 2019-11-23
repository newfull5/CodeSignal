def sortByHeight(a):
    index = []
    i = 0
    
    while True:
        if a[i] == -1:
            i += 1

        else:
            break

        if i == len(a):
            return a
    
    
    for i in range(0,len(a)):
        if a[i] == -1:
            index.append(i)

    a.sort()
    
    for i in range(0, len(a)):
        if a[i] != -1:
            a = a[i:]
            break
            

            
    for num in index:
        a.insert(num, -1)
        
    return a

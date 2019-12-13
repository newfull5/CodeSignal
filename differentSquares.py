def differentSquares(matrix):
    row = len(matrix)
    col = len(matrix[0])
    m = []
    
    for i in range(row-1):
        for j in range(col-1):
            kkk = [
                [matrix[i][j], matrix[i][j+1]],
                [matrix[i+1][j], matrix[i+1][j+1]]
            ]
            if kkk not in m:
                m.append(kkk)
                
                
    return len(m)

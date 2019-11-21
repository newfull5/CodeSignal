def matrixElementsSum(matrix):
    answer = 0
    
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if matrix[i][j] == 0:
                for k in range(i+1, len(matrix)):
                    matrix[k][j] = 0
                    
    for num in matrix:
        answer += sum(num)
        
    return answer

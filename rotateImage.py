def rotateImage(a):
    n = len(a)

    answer = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            answer[j][n-i-1] = a[i][j]
    return answer

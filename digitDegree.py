def digitDegree(n):
    n = str(n)
    cnt = 0
    while True:
        temp = 0
        if int(n) < 10:
            return cnt
        n = str(n)
        for i in range(0, len(n)):
            temp += int(n[i])

        n = temp
        cnt += 1

def phoneCall(min1, min2_10, min11, s):
    cnt = 0
    while s >= 0:
        cnt += 1
        if cnt == 1:
            s -= min1
        elif cnt > 1 and cnt < 11:
            s -= min2_10
        else:
            s -= min11
    return cnt-1
            


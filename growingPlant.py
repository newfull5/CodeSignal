def growingPlant(upSpeed, downSpeed, desiredHeight):
    day = 0
    cnt = 1
    day += upSpeed
    
    while True:
        if day >= desiredHeight:
            break
        day += upSpeed
        day -= downSpeed
        cnt += 1
            
    return cnt

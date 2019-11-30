def depositProfit(deposit, rate, threshold):
    cnt = 0
    while True:
        deposit += (deposit/100)*rate
        cnt += 1
        if deposit >= threshold:
            return cnt


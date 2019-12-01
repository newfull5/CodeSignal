def knapsackLight(value1, weight1, value2, weight2, maxW):
    if maxW >= weight1+weight2:
        return value1+value2
    else:
        if value1 >= value2 and weight1 <= maxW:
            return value1
        if value2 >= value1 and weight2 <= maxW:
            return value2
        if weight1 > maxW and weight2 > maxW:
            return 0
        if maxW >= weight1 and maxW >= weight2:
            return max(value1,value2)
        if maxW >= weight1 and maxW < weight2:
            return value1
        if maxW >= weight2 and maxW < weight1:
            return value2

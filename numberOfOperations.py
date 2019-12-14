def numberOfOperations(a, b):
    k = 0
    while True:
        if a % b == 0:
            a = a//b
            k += 1
        elif b % a == 0:
            b = b//a
            k += 1
        else:
            break
            
    return k

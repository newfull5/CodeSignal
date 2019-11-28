def evenDigitsOnly(n):
    n = str(n)
    for i in range(0, len(n)):
        if int(n[i]) % 2 == 1:
            return False
        
    return True

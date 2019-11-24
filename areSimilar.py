def areSimilar(a, b):
    cnt = 0
    if sorted(a) == sorted(b):
        for i in range(0, len(a)):
            if a[i] != b[i]:
                cnt += 1    
    else:
        return False
    
    if cnt == 2 or cnt == 0:
        return True
    else:
        return False
        

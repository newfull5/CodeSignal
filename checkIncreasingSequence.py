def checkIncreasingSequence(seq):
    for i in range(1, len(seq)):
        if seq[i-1] >= seq[i]:
            return False
        
    return True

def almostIncreasingSequence(sequence):
    j=0
    k=0
    i=1
    m=1
    jflag=0
    kflag=0

    dupsequence = list(sequence)

    while i < len(sequence):
        difference = sequence[i]-sequence[i-1]
        if (difference) <= 0:
            j = j+1
            del sequence[i]
            i = 0
            if j > 1:
               jflag = 1
               break

        i = i + 1

    while m < len(dupsequence):
        if (dupsequence[m]-dupsequence[m-1]) <= 0:
            k = k+1
            del dupsequence[m-1]
            m = 0
            if k > 1:
                kflag = 1
                break

        m = m + 1

    if kflag == 0 or jflag == 0:
        return True

    if jflag ==1 and kflag==1:
        return False

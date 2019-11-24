def alternatingSums(a):
    left = []
    right = []
    for i in range(0, len(a), 2):
        left.append(a[i])

    for i in range(1, len(a), 2):
        right.append(a[i])

    return [sum(left), sum(right)]

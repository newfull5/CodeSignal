def findEqual(sequence):
    if len(sequence) == len(set(sequence)):
        return False
    return True


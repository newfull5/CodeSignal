def variableName(name):
    for num in name:
        if num != '_':
            if not num.isnumeric():
                if ord(num) > 122 or 90 < ord(num) < 97 or ord(num) < 65:
                    return False

    if name[0].isnumeric():
        return False

    return True

def findEmailDomain(address):
    for i in range(0, len(address)):
        if address[-i] == '@':
            return address[-i+1:]

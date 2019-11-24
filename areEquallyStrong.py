def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if (yourLeft+yourRight) == (friendsLeft+friendsRight) and max(yourLeft,yourRight) == max(friendsLeft,friendsRight):
        return True
    else:
        return False

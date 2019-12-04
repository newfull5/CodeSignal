def validTime(time):
    if int(time[0:2]) < 24 and int(time[3:5]) < 60:
        if time == '24:00':
            return False
        return True
    else:
        return False
    

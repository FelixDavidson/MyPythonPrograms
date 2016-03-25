def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    elif not talking and (hour < 7 or hour > 20):
        return False
    else:
        return False

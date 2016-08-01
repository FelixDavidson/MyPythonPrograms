def is_power(a, b):
    if a == 0 or b == 0:
        return False
    elif b == 1:
        if a == 1:
            return True
        else:
            return False
    if a == 1 or (a/b == 1):
        return True
    elif a % b == 0 and a != 0:
        return is_power ( (a/b), b)
    else:
        return False

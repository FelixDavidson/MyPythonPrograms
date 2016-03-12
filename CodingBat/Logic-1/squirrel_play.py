def squirrel_play(temp, is_summer):
    if is_summer:
        return temp <= 100 and temp >= 60
    else:
        return temp <= 90 and temp >= 60

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif (date >= 8 and you >= 3) or (you >= 8 and date >= 3):
            return 2
    return 1

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    if num >= 5:
        while not num % 10:
            num =+ 1
        return num
    while not num % 10 and not num == 0:
        num =- 1
    return num
round_sum(16, 17 ,18)

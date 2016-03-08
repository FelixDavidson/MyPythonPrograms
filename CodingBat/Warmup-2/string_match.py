def string_match(a, b):
    amount = 0
    for i in range(len(a)-1):
        if a[i:i+2]  == b[i:i+2]:
            amount += 1
    print amount
'''
Old code
def string_match(a, b):
    amount = 0
    for i in range(len(a)):
        if (len(a[i:i+2]) == 2) and a[i:i+2]  == b[i:i+2]:
            amount += 1
    return amount
'''

def no_teen_sum(a, b, c):
    if 13 <= a <= 19 and a != 15 and a != 16:
        a = 0
    if 13 <= b <= 19 and b != 15 and b != 16:
        b = 0
    if 13 <= c <= 19 and c != 15 and c != 16:
        c = 0
    return a + b + c
# No need for extra function mainly because
#I didn't understand that part of the question
'''
def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n in [13, 14, 17, 18, 19]:
        return 0
    return n
'''

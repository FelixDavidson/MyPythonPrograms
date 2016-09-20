def while_countdown(n):
    while n >= 0:
        print n
        n -= 1
    print 'Blastoff!'

def for_countdown(n):
    for i in range(-1, n):
        print n
        n -= 1
    print 'Blastoff!'


while_countdown(10)
for_countdown(10)

def countdown(n):
    if n <= 0:
            print 'Blastoff!'
    else:
            print n
            countdown(n-1)

def do_n(obj, n):
    if n <=0:
        return
    else:
        obj(3)
        do_n(obj, n-1)

do_n(countdown, 3)

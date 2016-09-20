def square_root(a):
    epsilon = 0.0000001
    x = a / 2
    while True:
        print x
        y = (x + a/x) /2
        if abs(y-x) < epsilon:
            print 'This one ^'
            break
        x = y

square_root(100)
square_root(4)
square_root(9)
square_root(2132)

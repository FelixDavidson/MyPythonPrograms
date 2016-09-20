from math import sqrt

def square_root(a):
    epsilon = 0.0000001
    x = a / 2
    while True:
        y = (x + a/x) /2
        if abs(y-x) < epsilon:
            return y
            break
        x = y

def test_square_root(a):
    print a,
    print square_root(a),
    print sqrt(a),
    print square_root(a) - sqrt(a)

test_square_root(1.0)
test_square_root(2.0)
test_square_root(3.0)
test_square_root(4.0)
test_square_root(5.0)
test_square_root(6.0)
test_square_root(7.0)
test_square_root(8.0)
test_square_root(9.0)

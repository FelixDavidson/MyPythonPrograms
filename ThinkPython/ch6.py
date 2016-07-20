import math

# 6.1

def area(radius):
    return math.pi * radius**2

# 6.2

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsqared)
    return result

# 6.3

def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

# 6.4

def is_divisible(x, y):
    return x % y == 0

# 6.5

def factorial(n):
    space = ' ' * (4 * n)
    print space, 'factorial', n
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print space, 'returning', result
        return result

def fibonacci(n):
    if not isinstance(n, int):
        print 'Factorial is only defined for integers.'
        return None
    elif n < 0:
        print 'Factorial is not defined for negative integers.'
        return None
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

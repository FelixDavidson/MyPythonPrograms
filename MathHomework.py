# This is my math homework. Some (a lot) of it I left out. Just thought it be
# good to use it to learn more programming
def addition(x, y):
    """Takes two arguments and adds them"""
    added = x + y
    print added

def subraction(x, y):
    """Takes two arguments and subtracts the second from the first"""
    sub = x - y
    print sub

def mutiplication(x, y, z = 1):
# z is defaulted to 1 so you are able to do
# mutiplication with both 2 and 3 numbers
    """Takes two required arguments and one optional argument and multiplies them"""
    mult = x * y * z
    print mult

def divide(x, y):
    """Takes two arguments and divides the first by the second"""
    div = x / y
    print div

def problem(x, y, z):
    """Takes three arguments multiplies the first two and then adds the third"""
    print x * y + z

def iamsolazy(x, y, z):
    """Takes three arguments subtracts the first by the second then adds the third"""
    lazy = x - y + z
    print lazy

def average(x, y, z, a):
    """Takes four arguments find the average of the first three. Then finds the sum of
     the first three. Then find the number needed to get to a. Then gets a new average"""
    # aka the most retarded problem. My dumbass could realizes that I should floating points when using averages. Fixed it by getting rid of the problem
    oldav = (x + y + z) / 3
    tom = (x + y + z)
    neednum = (a * 4) - tom
    print oldav
    print neednum
    newav = (x + y + z + neednum) / 4
    print "%d + %d + %d + %d / 4 = %d" % (x, y, z, neednum, newav)

def more(a, b, c, d):
    """Takes four arguments divides the first by the second then subtracts the third
    times the fourth."""
    answer = a / b - c * d
    print answer

def whysomany(a, b, c, d, e):
    """Takes five arguments subtracts the second to the the power of the third from
    the first then multiplies that with the fourth and adds the fifth"""
    answer = a - b ** c * d + e
    print answer

def multidiv(x, y, z):
    """Takes three arguments multiplies the first and the second then divides by
    the third"""
    percent = x * z
    answer = percent / y
    print answer

def fire(p, s, pol, g, total):
    """Takes five arguments subtracts the sum of the first through fourth from the fifth"""
    f = total - (p + s + pol + g)
    print f

def absolute(x, y, z):
    """Takes three arguments adds the last two and divides by the first. Then does
    the same but with z equal to it's opposite"""
    answer = (z + y) / x
    print answer
    z = -z
    answer1 = (z + y) / x
    print answer1

mutiplication(-5, 3, 2)
problem(-6, -3, 2)
iamsolazy(82, 15, 35)
average(150, 210, 170, 180)
more(8, 4, 3, 2)
whysomany(12, 2, 2, 3, 5)
multidiv(18, 72, 100)
multidiv(12, 60, 100)
mutiplication(0.3, 5000000)
fire(10, 44, 30, 4, 100)
divide(-24.0, 18)
multidiv(8.0, 7, 3)
absolute(4.0, 5, 3)

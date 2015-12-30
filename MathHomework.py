# This is my math homework. Some (a lot) of it I left out. Just thought it be good to use it to learn more programming
def addition(x, y):
    added = x + y
    print added

def subraction(x, y):
    sub = x - y
    print sub

def mutiplication(x, y, z):
    mult = x * y * z
    print mult

def divide(x, y):
    div = x / y
    print div

def problem(x, y, z):
    print x * y + z

def iamsolazy(x, y, z):
    lazy = x - y + z
    print lazy


def average(x, y, z, a):
    # aka the most retarded problem. My dumbass could realizes that I should floating points when using averages. Fixed it by getting rid of the problem
    oldav = (x + y + z) / 3
    tom = (x + y + z)
    neednum = (a * 4) - tom
    print oldav
    print neednum
    newav = (x + y + z + neednum) / 4
    print "%d + %d + %d + %d / 4 = %d" % (x, y, z, neednum, newav)

mutiplication(-5, 3, 2)
problem(-6, -3, 2)
iamsolazy(82, 15, 35)
average(150, 210, 170, 180)

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

square(bob, 50)
def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, n)

def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)

polygon(bob, 100, 50)

def circle(t, r):
    t = 1
    r = 2

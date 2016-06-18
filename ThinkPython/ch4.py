from swampy.TurtleWorld import *
from math import pi

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

square(bob, 50)

def polygon(t, length, n):
    angle = 360.0/n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

polygon(bob, 50, 5)

def circle(t, r):
    cir = 2 * pi * r
    n = int(cir / 3) + 1
    length = cir / n
    polygon(t, length, n)

#circle(bob, 50)

def arc(t, r, angle):
    cir = 2 * pi * r
    n = int((cir / 3) + 1 * (angle/360.0))
    length = cir / n
    polygon(t, length, n)

arc(bob, 50, 180)

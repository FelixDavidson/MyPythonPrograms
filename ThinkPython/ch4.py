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

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, length, n):
    angle = 360.0/n
    polyline(t, n, length, angle)

polygon(bob, 50, 5)

def circle(t, r):
    arc(t, r, 360)

#circle(bob, 50)

def arc(t, r, angle):
    arc_length = 2 * pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

arc(bob, 50, 360)

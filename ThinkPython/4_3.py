import math
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

square(bob, 100)

def polygon(t,  n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

polygon(bob, 5, 50)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 10)
    print n
    polygon(bob, n, 20)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 10)
    step_length = arc_length / 2
    step_angle = float(angle) / 2
    polygon
circle(bob, 50)
wait_for_user()

from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
#bob.delay = 0.1

"""
4.3 Exercises
"""

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

#square(bob, 50)

def polyline(t, n, length, angle):
    """Draws n line segments with given length and
    angle (in degrees) between them. t is a turtle.
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, length, n):
    """Draws an n sided polygon with given length.
    t is a turtle.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)

#polygon(bob, 50, 5)

def circle(t, r):
    """Draws a circle. r is radius. t is turtle.
    """
    arc(t, r, 360)

#circle(bob, 50)

def arc(t, r, angle):
    """Draws an arc. r is radius. t is turtle.
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

#arc(bob, 50, 360)

"""
4.12 Turtle Flowers
"""

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0/n)

def move(t, length):
    pu(t)
    fd(t, length)
    pd(t)


#move(bob, -100)
#flower(bob, 7, 60.0, 60.0)

#move(bob, 100)
#flower(bob, 10, 40.0, 80.0)

#move(bob, 100)
#flower(bob, 20, 120.0, 20.0)

"""
4.12 Turtle Pies
"""

def isosceles(t, r, angle):
    y = r * math.sin(angle * math.pi / 180)

    rt(t, angle)
    fd(t, r)
    lt(t, 90+angle)
    fd(t, 2*y)
    lt(t, 90+angle)
    fd(t, r)
    lt(t, 180-angle)

def polypie(t, n, r):
    angle = 360.0
    for i in range(n):
        isosceles(t, r, angle/2)
        lt(t, angle)

def draw_pie(t, n, r):
    polypie(t, n, r)
    pu(t)
    fd(t, r*2 + 10)
    pd(t)

size = 40
draw_pie(bob, 5, size)
draw_pie(bob, 6, size)
draw_pie(bob, 7, size)
draw_pie(bob, 8, size)
die(bob)

world.canvas.dump()
wait_for_user()

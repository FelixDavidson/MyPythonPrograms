from swampy.TurtleWorld import *
import math

#world = TurtleWorld()
#bob = Turtle()
#bob.delay = 0.1

"""
4.3 Exercises
"""

def square(t, length):
    """Draws a square.

    t: Turtle
    length: length of sides
    """
    for i in range(4):
        fd(t, length)
        lt(t)

#square(bob, 50)

def polyline(t, n, length, angle):
    """Draws n line segments with given length and
    angle (in degrees) between them.

    t: Turtle
    n: number of sides
    length: length of sides
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, length, n):
    """Draws an n sided polygon with given length.

    t: Turtle
    length: Length of sides
    n: Number of sides
    """
    angle = 360.0/n
    polyline(t, n, length, angle)

#polygon(bob, 50, 5)

def circle(t, r):
    """Draws a circle.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)

#circle(bob, 50)

def arc(t, r, angle):
    """Draws an arc.

    t: Turtle
    r: radius
    angle: Angle
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
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
    """Draws a petal using arc.

    t: Turtle
    r: radius of arcs
    angle: angle that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)

def flower(t, n, r, angle):
    """Draws a flower using petal.

    t: Turtle
    n: number of petals
    r: radius of arcs
    angle: angle that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0/n)

def move(t, length):
    """Moves the Turtle (t) forward (length) units with pen up.
    Finishes with pen down.
    """
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
    """Draws an isosceles triangle with top angle (angle).

    t: Turtle
    r: length of equal legs
    angle: angle of top vertex
    """
    y = r * math.sin(angle * math.pi / 180)
    # Part of base length based on angle and side lengths

    rt(t, angle)
    fd(t, r)
    lt(t, 90+angle)
    fd(t, 2*y)
    lt(t, 90+angle)
    fd(t, r)
    lt(t, 180-angle)

def polypie(t, n, r):
    """Draws a pie divied into radial segments.

    t: Turtle
    n: number of segments
    r: length of raidal spikes
    """
    angle = 360.0
    for i in range(n):
        isosceles(t, r, angle/2)
        lt(t, angle)

def draw_pie(t, n, r):
    """Draws a pie, then moves to the right leaving no trial.
    Finishes with pen down.

    t: Turtle
    n: number of segments
    r: length of radial spikes
    """
    polypie(t, n, r)
    pu(t)
    fd(t, r*2 + 10)
    pd(t)

#size = 40
#draw_pie(bob, 5, size)
#draw_pie(bob, 6, size)
#draw_pie(bob, 7, size)
#draw_pie(bob, 8, size)
#die(bob)

#world.canvas.dump()
#wait_for_user()

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def square(t, length):
    t = Turtle()
    for i in range(4):
        fd(t, length)
        lt(t)

square(bob, 50)

def polygon(t, length, n):
    t = Turtle()
    for i in range(5):
        fd(t, 100)
        lt(t, 360/n)

polygon(bob, 50, 5)

def circle(

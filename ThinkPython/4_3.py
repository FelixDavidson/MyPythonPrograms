from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

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
    

circle(bob)

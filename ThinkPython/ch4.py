from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def square(t):
    t = Turtle()
    for i in range(4):
        fd(t, 100)
        lt(t)

square(bob)
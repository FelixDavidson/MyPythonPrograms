from swampy.TurtleWorld import *

def koch(t, length):
    fd(t, length/3)
    lt(t, 60)
    fd(t, length/3)
    rt(t, 120)
    fd(t, length/3)
    lt(t, 60)
    fd(t, length/3)
    rt(t, 120)

def snowflake(t, length):
    koch(t, length)
    koch(t, length)
    koch(t, length)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

snowflake(bob, 60)
wait_for_user()

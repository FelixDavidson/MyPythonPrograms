from swampy.TurtleWorld import *

def koch(t, length):
    if length < 3:
        fd(t, length)
        return
    n = length / 3.0
    koch(t, n)
    lt(t, 60)
    koch(t, n)
    rt(t, 120)
    koch(t, n)
    lt(t, 60)
    koch(t, n)

def snowflake(t, length):
    for i in range(3):
        koch(t, length)
        rt(t, 120)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0

snowflake(bob, 120)
wait_for_user()

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

fd(bob, 100)
lt(bob)
fd(bob, 100)
lt(bob)
fd(bob, 100)
lt(bob)
fd(bob, 100)

wait_for_user()

for i in range(4):
    print 'Hello!'

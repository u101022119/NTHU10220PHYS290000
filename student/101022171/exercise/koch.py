from swampy.TurtleWorld import *

world = TurtleWorld()

bob = Turtle()
bob.delay = 0.001

def koch(t, length):
    if length <=2 :
        fd (t, length)
        return
    koch(t, length/3)
    lt(t, 60)
    koch(t, length/3)
    rt(t, 120)
    koch(t, length/3)
    lt(t, 60)
    koch(t, length/3)


koch(bob, 540)

wait_for_user()

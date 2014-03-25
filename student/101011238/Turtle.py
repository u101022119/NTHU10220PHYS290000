import math

from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()



#length = input('Length:')
#n = input('n:')

#for i in range(50):
#    fd(bob, length)
#    lt(bob, 360/n)
#    bob.delay = 0.01

n=3
side=1000
r=150
length=2 * math.pi * r/1000

def polygon_(t, side, length,n):
    angle = 360.0 / 1000
    for i in range(int(side/(n))):

        fd(t, length)
        lt(t, angle)


        
        t.delay = 0.0001

def polygon(t, side, length,n):
    angle = 360.0 / 1000
    for i in range(int(side/(n))):
        fd(t, length)

        lt(t, angle)

        t.delay = 0.0001

polygon_(bob, 1000, length,n)

lt(bob,90)



polygon(bob, 1000, length,n)




wait_for_user()



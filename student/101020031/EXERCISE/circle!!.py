from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob

import math

def poly(t,n,l):
    angle=360.0/n
    for i in range(1000000):
        fd(t,l)
        lt(t,angle)




def circ(t,r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1

    l=circumference / n
    poly(t,n,l)


def arc(t,r,angle):
    arc_length = 2 * math.pi * r * angle / 360
    n=int(arc_length / 3) +1
    step_length = arc_length / n

    step_angle = float(angle) / n


    for i in range(n):
        fd(t,step_length)
        lt(t,step_length)

    

bob.delay =0.1


for i in range(10000):
    lt(bob,36)
    fd(bob,50)
    lt(bob,180)
    fd(bob,50)
    rt(bob,36)
    fd(bob,50)
    lt(bob,180)
    fd(bob,50)
    rt(bob,36)
    fd(bob,50)
    lt(bob,180)
    fd(bob,50)
    rt(bob,36)
    fd(bob,50)
    lt(bob,180)
    fd(bob,50)
    rt(bob,36)
    fd(bob,50)
    lt(bob,126)
    fd(bob,100* math.cos(54.0/180.0* math.pi))
    lt(bob,72)
    fd(bob,100* math.cos(54.0/180.0* math.pi))
    lt(bob,72)
    fd(bob,100* math.cos(54.0/180.0* math.pi))
    lt(bob,72)
    fd(bob,100* math.cos(54.0/180.0* math.pi))
    lt(bob,72)
    fd(bob,100* math.cos(54.0/180.0* math.pi))
    lt(bob,126)
    fd(bob,50)
    rt(bob,72)
    
    

    
    
    
    
    













wait_for_user()

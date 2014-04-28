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

    

bob.delay =0.01

def polyline(t,n,l,a):
    for i in range(n):
        fd(t,l)
        lt(t,a)

def polygon(t,n,l):      #繞一圈
    a=360.0 / n
    polyline(t,n,l,a)

def arc1(t,r,angle):     #繞特定角度
    arc_length = 2 * math.pi * r * angle / 360
    n=int(arc_length / 3) +1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t,n,step_length,step_angle)

arc1(bob,100,120)


    

        


    

    
    
    
    
    













wait_for_user()

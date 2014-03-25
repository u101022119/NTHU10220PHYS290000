from swampy.TurtleWorld import *
import math
world=TurtleWorld()
bob=Turtle()
print bob

ted=Turtle()
print ted
kid=Turtle()
print kid
bob.delay=0.01
ted.delay=0.01
def circle1(t,n,k,l):
    angle=360.0/n*k
    for i in range(n):
        lt(t,angle)
        fd(t,l)
    return circle1
def polyline(t,n,length,angle):
    for i in range(n):
        fd(t,length)
        lt(t,angle)
        
def polygon(t,n,length):
    angle=360.0/n
    polyline(t,n,length,angle)
 
def arc(t,r,angle):
    arc_length=2*math.pi*r*angle/360
    n=int(arc_length/3)+1
    step_length=arc_length/n
    step_angle=float(angle)/n
    polyline(t,n,step_length,step_angle)
    
def circle2(t,r):
    arc(t,r,360)
def flower(t,r,p):
    for i in range(p) :
        a=180-180*p/(p-2)
        rt(t,a)
        arc(t,r,180)

arc(ted,25,90)
flower(ted,25,5)



def snow(t,r,a):
        fd(t,r)
        lt(t,120)
        fd(t,r)
        rt(t,120)
        fd(t,r)
        lt(t,60)
        fd(t,r)
        rt(t,120)
        fd(t,r)
        lt(t,60)
        fd(t,r)
        rt(t,120)
        fd(t,r)
        lt(t,120)
        fd(t,r+10)
        rt(t,60)
        fd(t,r+10)
snow(bob,10,100)
snow(bob,10,100)
snow(bob,10,100)
snow(bob,10,100)
snow(bob,10,100)
snow(bob,10,100)




wait_for_user()

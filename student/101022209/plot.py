from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob
# fd(bob,100)

# lt(bob)

# fd(bob,100)

# for i in range(4):
#     fd(bob,100)

# lt(bob)
import math
def square(t,l):
    for i in range(4):
        t.delay=0.01
        fd(t,l)
        lt(t)
        

def polygon(t,n,l):
    a=360.0/n
    for i in range(n):
        bob.delay=0.01
        fd(t,l)
        lt(t,a)
        

def circle(t,r):
    k=2*math.pi*r
    n=300
    l=k/n
    polygon(t,n,l)
    

def arc(t,angle):
    t.delay=0.0001
    n = int( angle / 0.36 )
    for i in range(n):
        fd(t,0.2)
        lt(t,0.36)

circle(bob,50)


    







wait_for_user()





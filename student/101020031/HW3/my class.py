class Point(object):
    """pass"""
class Rectangle(object):
    """pass"""

def distance_between_points(p1,p2):
    dx=(p1.x)-(p2.x)
    dy=(p1.y)-(p2.y)
    ds=(dx**2 + dy**2)**(1.0/2)
    print ds

import copy

def move_rectangle1(rec,dx,dy):
    rec.corner.x = rec.corner.x + dx
    rec.corner.y = rec.corner.y + dy

def move_rectangle2(rec,dx,dy):
    rec1=copy.deepcopy(rec)
    rec1.corner.x=rec1.corner.x + dx
    rec1.corner.y=rec1.corner.y + dy
    return rec1

    
    



a=Point()
a.x=0
a.y=0

b=Point()
b.x=3.0
b.y=4.0


distance_between_points(a,b)

c=Rectangle()
c.corner=Point()
c.corner.x=3.0
c.corner.y=4.0

move_rectangle1(c,3,4)
move_rectangle2(c,3,4)



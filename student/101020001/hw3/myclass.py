


import math 

class Point():
    """Points in 2D-space"""
class Rectangle():
    '''Rectangles in 2D-space'''

P1=Point()
P2=Point()

P1.x=3.0
P1.y=4.0
P2.x=6.0
P2.y=8.0
def distance_between_points(P1,P2):
    k=math.sqrt((P1.x-P2.x)**2 + (P1.y-P2.y)**2)
    print "distance between points is P1&P2 is",k

distance_between_points(P1,P2)

square=Rectangle()
square.w=100.0
square.h=200.0
square.corner=Point()
square.corner.x=0.0
square.corner.y=0.0
dx=5.0
dy=7.0
def move_rectangle(square,dx,dy):
    square.corner.x+=dx
    square.corner.y+=dy
    print "new Rectangle's corner is",'(%g,%g)'%(square.corner.x,square.corner.y)
    
move_rectangle(square,dx,dy)
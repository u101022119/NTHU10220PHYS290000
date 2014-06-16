import math
import copy
class point(object):
    """just a point"""
class rectangle(object):
    """just a retangle"""
    corner = point()
def distance_between_points(p1,p2):
    dx=p1.x-p2.x
    dy=p1.y-p2.y
    return math.sqrt(dx**2+dy**2)
def move_rectangle(rect,dx,dy):
    new_rect=copy.copy(rect)
    new_rect.corner.x+=dx
    new_rect.corner.y+=dy
    return new_rect
rect1=rectangle()
rect1.corner.x=0
rect1.corner.y=0
rect2=move_rectangle(rect1,1,1)
print rect2.corner.x,rect2.corner.y

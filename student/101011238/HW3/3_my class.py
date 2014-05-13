import copy
import math

class point(object):
    """Represents a point in 2-D space."""

class rectangle(object):
    """Represents a rectangle.
    attributes: width, height, corner.
    """

a = point()
a.x = 0.0
a.y = 0.0

b = point()
b.x = 3.0
b.y = 4.0

box = rectangle()
box.width = 100.0
box.height = 200.0
box.corner = point()
box.corner.x = 0.0
box.corner.y = 0.0

def print_point(p):
    print '(%g, %g)' % (p.x, p.y)

def distance_between_points(a,b):
    distance = math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)
    return distance
    
def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

def move_rectangle_(rect, dx, dy):
    global newbox
    newbox = copy.deepcopy(box)
    newbox.corner.x += dx
    newbox.corner.y += dy

print_point(a)
print_point(b)
print 'The distance between a and b is',distance_between_points(a,b)
print ''

move_rectangle_(box, 10, 10)
print 'box.corner:'
print_point(box.corner)
print 'newbox.corner:'
print_point(newbox.corner)

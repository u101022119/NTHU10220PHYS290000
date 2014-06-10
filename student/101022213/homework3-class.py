
class Point(object):    
    """Represents a point in 2-D space."""
    
blank1 = Point()
blank2 = Point()

def print_point(p):
    print '(%g, %g)' % (p.x, p.y)
    

class Rectangle(object):
    """Represents a rectangle.attributes: width, height, corner."""
    
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

blank1.x=a1 = int(raw_input('Put the first point x:'))
blank1.y=a2 = int(raw_input('Put the first point y:'))

blank2.x=b1 = int(raw_input('Put the second point x:'))
blank2.y=b2 = int(raw_input('Put the second point y::'))

def distance_between_points(a1,a2,b1,b2):
    d=(a1-b1)**2+(a2-b2)**2
    distance=d**0.5
    return distance



def move_rectangle(rect,dx,dy):
    rect.corner.x+=dx
    rect.corner.y +=dy


newcenter = Rectangle()
newcenter.width = box.width
newcenter.height = box.height
newcenter.corner = Point()
newcenter.corner.x = box.corner.x
newcenter.corner.y = box.corner.y    

def creact_new_rectangle(dx,dy):
    newcenter.corner.x +=dx
    newcenter.corner.y +=dy
    
    print_point(newcenter.corner)
    



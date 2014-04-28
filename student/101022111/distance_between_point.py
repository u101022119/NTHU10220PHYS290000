import math

class Point(object):
    """Represents a point in 2-D space."""
blank=Point()
blank.x=float(raw_input('x coordinate:'))
blank.y=float(raw_input('y coordinate:'))

def distance_between_point():
    distance=math.sqrt(blank.x**2+blank.y**2)
    print distance
distance_between_point()        
    

import math

def convert_polar(x,y):
    d = (x*x+y*y)**0.5
    angle = math.atan(y/x)*360/(2*math.pi)

    print "the distance is",d,"the angle is",angle

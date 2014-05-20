import math 

def convert_polar():
    x = float(raw_input("Enter the x coordinate: "))
    y = float(raw_input("Enter the y coordinate: "))
    R = (x**2+y**2)**(1.0/2)
    angle = math.atan(y/x)*180/math.pi
    print "(",R,angle,"degree)"

import math
def convert_polar():
    print 'For the Cartesian coordinates, print x,y of a point in 2D space, and it will calculate to corresponding polar coordinates. '
    x = float(raw_input('Enter x = '))
    y = float(raw_input('Enter y = '))
    print 'the point you enter in Cartesian coordinates is (',x,',',y,')\n', 
    r =(x**2+y**2)**(0.5)
    t =math.atan(y/x)
    print 'the point transforms into polar coordinates is (',r,',',t,')'
convert_polar()

import math
def convert_polar():
    print 'the is a program that can change Cartesian coordinates into polar coordinates'
    x = float(raw_input('Enter x value = '))
    y = float(raw_input('Enter y value = '))
    print 'the point you enter on Cartesian coodinates is (',x,',',y,')\n', 
    r =(x**2+y**2)**(0.5)
    t = math.atan(y/x)
    print 'the point transforms into polar coodinates is (',r,',',t,')'
convert_polar()

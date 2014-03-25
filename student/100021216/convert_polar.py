import math

print 'Enter the Cartesian coordinates (x,y)'
x=float(input('x='))
y=float(input('y='))

if x==0 and y==0:
    print 'This point is undefined in polar coordinates.'
else:
    r=math.sqrt(x*x+y*y)
    theta=180/math.pi*math.atan2(y,x)
    if theta<0:
        theta+=360
        print 'The corresponding polar coordinates is ('+str(r)+','+str(theta)+').'
    else:
        print 'The corresponding polar coordinates is ('+str(r)+','+str(theta)+').'

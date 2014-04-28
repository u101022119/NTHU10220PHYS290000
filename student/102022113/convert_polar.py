import math

x=float(raw_input('The x-coordinate:'))
y=float(raw_input('The y-coordinate:'))

r=math.sqrt(x**2+y**2)

if r==0:
    print 'The corresponding polar coordinates is (',0,',',0,'degrees)'
else:
    theta=math.acos(x/r)*180/math.pi
    if y>=0:
        print 'The corresponding polar coordinates is (',r,',',theta,'degrees)'
    else:
        if x<0:
            print 'The corresponding polar coordinates is (',r,',',90+theta,'degrees)'
        elif x==0:
            print 'The corresponding polar coordinates is (',r,',',180+theta,'degrees)'
        else:
            print 'The corresponding polar coordinates is (',r,',',270+theta,'degrees)'

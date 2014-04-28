import math
x = float(raw_input('Input x:'))
y = float(raw_input('Input y:'))

print 'Cartesian (', x,',',y, ')'
r = (x**2+y**2)**(1.0/2)

theta = math.acos(x/r)

print 'Polar (r=',r,', theta=',theta ,')'

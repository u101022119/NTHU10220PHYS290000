import math
x=float(raw_input('x='))
y=float(raw_input('y='))
r=math.sqrt(x*x+y*y)
angle=float(math.atan(y/x)/math.pi*180)
print 'the distance=',r
print 'the angle=',angle

import math
x=float(raw_input('enter the value of the x coordinate:'))
y=float(raw_input('enter the value of the y coordinate:'))
r=math.sqrt(x**2+y**2)
theta=math.atan(y/x)*180/math.pi
print 'the corresponding polar coordinates (r,theta) is:','(',r,',',theta,')','theta given in degrees'

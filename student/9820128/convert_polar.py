import math
x = input('x= ')
y = input('y= ')
r = (x**2+y**2)**0.5
m = math.atan2(y,x)*180/math.pi
print '(',r,',',m,')'

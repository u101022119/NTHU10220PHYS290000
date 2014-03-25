import math
x=raw_input('I need the x coordinate!\n')
y=raw_input('I need the y coordinate!\n')
x=float(x)
y=float(y)
s=math.atan(y/x)/math.pi*180
r=math.sqrt(x**2+y**2)
print 'the radius is ---->',r
print 'the angle in degree is ---->',s

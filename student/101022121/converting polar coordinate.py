import math
x=raw_input('enter the coordinate x\n')
y=raw_input('enter the coordinate y\n')
x=float(x)
y=float(y)
s=math.atan(y/x)/math.pi*180
print 'the angle in degrees is', s

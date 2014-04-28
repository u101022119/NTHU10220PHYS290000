import math
x=input('x=')
y=input('y=')
r=math.sqrt(x*x+y*y)
theta=math.acos(x/r)
if y<0:
    theta+=math.pi
print ('r=%f' % r)
print ('theta=%f' % theta)

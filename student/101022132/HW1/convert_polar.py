import math

x=raw_input('x=')
y=raw_input('y=')
x=float(x)
y=float(y)
r=x**2+y**2
r=float(r)
g=y/x
g=float(g)
a=math.atan(g)
a=float(a)
b=a*180/math.pi
b=float(b)
print '(',r,',',b,'«×)'

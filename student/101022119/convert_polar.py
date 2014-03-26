import math
def a(b,c):
    t=c/b
    t=math.atan(t)
    t=t*180/math.pi
    r=(b**2+c**2)**(1.0/2)
    return [r,t]

x=float(raw_input('x='))
y=float(raw_input('y='))

print '[r,degree]=',a(x,y)

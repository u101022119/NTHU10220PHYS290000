import math
x=input("x=")
y=input("y=")

def convert_polar(x,y):
    r=( x**2 + y**2)**(1.0/2.0)
    a= math.atan2(y,x)*180/math.pi
    print "the radius is",r,"the angle is",a

print convert_polar(x,y)
   

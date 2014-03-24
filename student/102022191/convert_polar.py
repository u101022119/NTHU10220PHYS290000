import math

x=float(raw_input("x coordinate\n"))
y=float(raw_input("y coordinate\n"))

r=math.sqrt(x*x+y*y)

if abs(x)>1**(-9):
    angle = math.atan(y/x)#in radian
    angle *= 180.0/math.pi#in degree
    if x>0:
        if y<0:
            angle += 360.0
    else:
        angle += 180.0 
else:
    angle = math.asin(y/r)*180.0/math.pi
    if angle<0:
        angle += 360.0

print "r=" , r , "angle=" , angle , "degree(s)"

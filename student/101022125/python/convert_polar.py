import math
x = float( raw_input("Enter x: ") )
y = float( raw_input("Enter y: "))
r = math.hypot(x,y)
theta = math.acos(x/r)
d=theta*180/math.pi
print "r=", r, "d= ", d

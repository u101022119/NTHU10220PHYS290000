#6.convert_polar.py
print "give me the coordinates in Cartesian,I will give you that in polar"
x=float(raw_input('give me x: '))
y=float(raw_input('give me y: '))
r=(x**2+y**2)**0.5
import math as m
theta=m.atan(y/x)*180.0/m.pi
print '''(r,theta)=(%g,%g)'''%(r,theta)

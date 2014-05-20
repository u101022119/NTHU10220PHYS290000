import math
x=float(raw_input('What is your X:'))
y=float(raw_input('What is your Y:'))
r=(x**2+y**2)**(1/2.0)
theta=math.atan(x/y)*180/math.pi
print 'r-coordinate is:',r,'theta-coordinate is:',theta

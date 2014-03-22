#Homework 1 exercise 6
x = float(raw_input('the x-coordinate is:'))
y = float(raw_input('the y-coordinate is:'))
r = (x**2 + y**2)**(1/2.0)
import math
theta = math.atan(y/x) * 180/math.pi

print 'the r-coordinate is', r
print 'the theta-coordinate is', theta, 'degrees'

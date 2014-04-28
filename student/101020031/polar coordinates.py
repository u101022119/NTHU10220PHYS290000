import math
x=input('Please enter x:')
y=input('Please enter y:')

r=(x**2+y**2)**(0.5)
angle=math.atan(y/x)*180/math.pi

print 'In polar coordinates,your r is',r,',your angle is',angle,'degrees'

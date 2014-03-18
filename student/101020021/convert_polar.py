
import math


x=float(raw_input('enter x : '))
y=float(raw_input('enter y : '))

print 'r = ',(x**2+y**2)**(1.0/2)
print 'theta(degree) = ',math.asin (y/(x**2+y**2)**(1.0/2))/math.pi*180


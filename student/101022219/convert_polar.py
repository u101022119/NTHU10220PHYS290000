x = float (raw_input('Enter the value of x coordinate :'))
y = float (raw_input('Enter the value of y coordinate :'))
import math
r = math.sqrt(x**2 + y**2)
theta = math.atan(y/x)*180/math.pi
print 'The corresponding polar coordinates is',[r,theta], 'theta given in degrees'

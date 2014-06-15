
x=float(raw_input('enter x component:'))
y=float(raw_input('enter y component:'))
r=(x**2.0+y**2.0)**0.5

import math
theata=math.atan(y/x)/(2*math.pi)*360.0
print 'the polar is (',r,',',theata,'degrees)'

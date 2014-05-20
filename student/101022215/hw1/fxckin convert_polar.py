import math
x=float(raw_input('x?'))
y=float(raw_input('y?'))
print 'the polar coordinate u ask is (r(length), theta(angle))= (', (x**2+y**2)**(0.5), ',',math.atan(y/x)*360/(2*math.pi),')' 

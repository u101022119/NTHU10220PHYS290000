import math
x=float(raw_input('give me x'))
y=float(raw_input('give me y'))
print "then, it's polar coordinate (r(length),theta(angle))= (",(x**2+y**2)**(0.5),",",math.asin(y/(x**2+y**2)**(0.5))*360/(2*math.pi),")"

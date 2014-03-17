# proof: If we use the Newtonian gravitational formula: GMm/r^2 = m*4*pi^2*r/T^2 and solve for r, we have r = (GMT^2/(4*pi^2))^(1/3) QED.

import math
t = float(raw_input('ENTER THE DESIRED VALUE OF THE PERIOD IN SECONDS OF THE SATELLITE: '))
G = 6.67*10**(-11)
M = 5.97*10**24
R = 6417*10**3
h = (G*M*t**2/4/math.pi**2)**(0.333333333333333333333333333333333333333333333333333333333333333)- R
print "The constant G is ",G
print "The constant M is ",M
print "The constant R is ",R
print "The attitude h above the Earth’s surface that the satellite must have is", h, "meters."




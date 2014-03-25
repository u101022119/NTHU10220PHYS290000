# v = 2* pi* r/ T
# F = m* r* 4* (pi**2)/ (T**2) = G* M* m/ (r**2)
# r = (G* M* (T**2)/(4* (pi**2)))**(1/3)
# h = r-R = (G* M* (T**2)/(4* (pi**2))**(1/3) - R
import math
T = input('Please enter your period:')
G = 6.67* (10**-11)
M = 5.97* (10**24)
R = 6.417* (10**6)
r_upper = G* M* T* T
r_lower = 4* (math.pi**2)
r = (r_upper/r_lower)**(1.0/3)
h = r -R
print h

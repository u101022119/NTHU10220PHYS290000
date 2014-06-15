

import math as m
G = 6.67*10**(-11)
M = 5.97*10**24 
R = 6417.0*1000 
T = input('Please enter the priod T (s) :')
print 'If a satellite run in a circular orbit around the Earth once every T second,'
h = ((G*M*T**2)/(4*m.pi))**(1.0/3.0) - R
print 'then the satellite must at',h, 'meters'

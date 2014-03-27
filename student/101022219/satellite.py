T = float ( raw_input('Enter the period of the satellite:'))
import math
G = 6.67*10**-11
M = 5.97*10**24
R = 6410

h = ((G*M*T**2)/(4*math.pi**2))**(1/3.0) - R

print 'The altitude of the satellite is', h, 'meters'

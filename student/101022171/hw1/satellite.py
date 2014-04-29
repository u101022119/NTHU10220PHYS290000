#File: satellite.py
#HW1_EX5_Altitude_of_a_satellite
#Due: 3/25/2014
#Author: 101022171

import math

G = 6.67 * 10**-11
M = 5.97 * 10**24
R = 6417.0

t = float( input('Enter the period T of the satellite in seconds. >:'))

h = ((G*M*t**2)/(4*math.pi**2))**(1.0/3) - R

print "The satellite is about %.2f km above the Earth¡¦s surface with period %.1fs." % (h, t)

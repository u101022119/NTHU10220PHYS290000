
T = float(raw_input('the desired period of the orbit is(in seconds):'))
G = 6.67 * 10**(-11)
M = 5.97 * 10**24
R = 6417
import math
h = ((G * M * T**2)/(4 * math.pi**2))**(1/3.0) - R

print 'the altitude of the given period,', T, 'seconds, is', h, 'meters'

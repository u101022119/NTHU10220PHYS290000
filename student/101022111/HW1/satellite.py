T = float(raw_input('the period of the orbit is(s):'))
G = 6.67 * 10**(-11)
M = 5.97 * 10**24
R = 6417
import math
h = ((G * M * T**2)/(4 * math.pi**2))**(1/3.0) - R

print 'when the period is:', T ,'the height is:',h,'(m)'

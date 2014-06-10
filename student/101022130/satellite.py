t = float(raw_input('enter a value of period of the satellite: '))

import math

h=((t*t*6.67*(10**(-11))*5.97*(10**24)/4.0/3.14/3.14)**(1.0/3.0))-6417000


print 'the altitude of a satellite',h

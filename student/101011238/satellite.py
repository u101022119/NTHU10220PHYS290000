import math

G = 6.67*(10**-11)
M = 5.97*(10**24)
R = 6.417*(10**6)

T = input('Enter T(second):')

h = (G*M*(T**2)/(4*(math.pi)**2))**(1.0/3.0)-R

print 'h =',h

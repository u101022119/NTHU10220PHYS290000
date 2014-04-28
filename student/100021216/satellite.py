import math

print 'A satellite is to be launched into a circular orbit around the Earth'

G=6.67*10**-11
M=5.97*10**24
R=6417000.0
T=float(input('Enter the period(in sec) of the satellite orbits the Earth once:'))

h=(((G*M*T**2)/(4*math.pi**2))**(1.0/3))-R


if T**2<((4*math.pi**2*R**3)/(G*M)):
    print 'The satellite would not orbit the Earth once in '+str(T)+' second(s)'
else:
    print 'The attitude above the Earth¡¦s surface of the satellite is '+str(h)+' meter(s)'
    

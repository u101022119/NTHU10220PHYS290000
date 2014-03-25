import math
T=raw_input('input satelite time:')
T=float(T)
G=6.67*10**(-11)
M=5.97*10**24
R=6417
h=((G*M*T**2/(4*math.pi**2))**(0.333333333333333)/1000)-R
print 'height=',h,'km'

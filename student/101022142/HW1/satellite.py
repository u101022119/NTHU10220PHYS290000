#5.satellite.py

print "h=(GMT^2/4PI^2)^(1/3)-R"
T=float(raw_input("give me the desire T in seconds"))
G=6.67*10**(-11)
M=5.97*10**24
R=6417000.0
import math as m
h=(G*M*T**2/(4*(m.pi)**2))**(1.0/3)-R

print 'the attitude is',h,'meters'

#notice the power is 1.0/3 not 1/3

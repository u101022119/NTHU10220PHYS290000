import math
t=input('please enter the period of a satellite around the Earth:')

G=6.67*10**(-11)
M=5.97*10**24
R=6417000

h=(G*M*t*t/4/(math.pi**2))**(1.0/3)-R

print 'the attitude of a satellite around the Earth is',h,'m'

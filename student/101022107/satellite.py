T=float(raw_input('enter a value of a period of the satelliate:'))
import math
G=6.67*10**-11
M=5.97*10**24
R=6417000
h=((G*M*T**2)/4*math.pi*math.pi)**1/3-R
print 'the constant G is:',G,'m^3/kg/s^2'
print 'the constant M is:',M,'kg'
print 'the constant R is:',R,'m'
print 'the altitude of the satelliate is: ',h,'m'

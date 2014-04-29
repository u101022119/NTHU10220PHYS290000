import math
G=6.67*10**(-11)
M=5.97*10**24
R=6417000.0
T=float(raw_input('Enter the desired time\n'))
h=(G*M*T**2/(4*(math.pi)**2))**(1.0/3)-R
print h 

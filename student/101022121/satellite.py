import math
T=raw_input('How long in second does the satellite orbit the Earth one time?\n')
T=int(T)
h=(6.67*(10**(-11))*5.97*(10**24)*(T**2)/(4*(math.pi**2)))**(1.0/3)-6417000

print h

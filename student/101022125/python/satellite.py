import math
T = float( raw_input("Enter T: ") )
G = 6.67*(10**-11)
M = 5.97*(10**24)
R = 6417
pi2 = math.pi**2
h=(G*M*T**2/4/pi2)**0.3333333-R
print "height the satellite orbits the planet  is",h,"meters"

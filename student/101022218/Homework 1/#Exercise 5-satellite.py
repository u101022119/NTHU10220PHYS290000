import math
T=float(raw_input("enter the desired value of time t:\n"))
G=6.67*10**(-11)
M=5.97*10**(24)
R=6417000
h=float(((G*M*T**2)/(4*(math.pi**2)))**(0.33333333)-R)
print"the attitude of the satellite is",h, "(m)"

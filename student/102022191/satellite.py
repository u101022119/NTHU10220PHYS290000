import math

G=6.67*(10**(-11))#m^3kg^-1s^-2
M=5.97*(10**24)#kg
R=6417.0#km

T=float(raw_input("Please input the period(in second)\n"))

total_height = (G*M*T**2/(4.0*math.pi**2))**(1.0/3.0)

h=total_height-R

print h , "m"

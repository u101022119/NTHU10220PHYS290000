T=input("Enter the desired value of T for th satellite : ")
import math
G=6.67*10**(-11)
M=5.97*10**(24)
R=6417000
h=(G*M*T**2/4/math.pi**2)**(0.3333333333)-6417000
print "The height of the staellite is",h, "meters"

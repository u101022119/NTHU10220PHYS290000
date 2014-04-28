
import math
T = float( raw_input("Enter the value of period: ") )
G = 6.67*10**(-11)
M = 5.97*10**24
R = 6417*10**3
a = G*M*T**2
b = 4*math.pi**2
h = (a/b)**(0.33333333333333333333333333333333333)-R
print "The attitude above the Earth's surface for", T, "is", h

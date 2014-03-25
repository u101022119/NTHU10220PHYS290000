import math
G=6.67*(10**(-11))
M=5.97*(10**2)
R=6417
T=float(raw_input("Put the period: "))
def satellite(T):
    h=(G*M*(T**2)/4/(math.pi**2))**(1/3)-R
    return h
print satellite(T)

import math
def satellite(T):
    G=6.67*10**-11
    M=5.97*10**2
    R=6.417*10**6
    pi=(math.pi)
    h=((G*M*T**2)/(4*pi**2))**(1.0/3)
    print h,'m'
T=float(raw_input('enter T(in s):'))
satellite(T)
 

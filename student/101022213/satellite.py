import math

def satellite(T):
    G = 6.67*(10**-11)
    M = 5.97*(10**24)
    R = 6417000
    
    x= G*M*T*T
    y= 4*(math.pi)*(math.pi)
    z= (x/y)**(1.0/3)
    H = z - 6417000
    if H <0:
        print "this period time is too small"
    else:
        print "the attitude h above the Earth¡¦s surface is",H

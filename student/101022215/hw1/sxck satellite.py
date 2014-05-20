
G=6.67*(10**(-11))
M=5.97*((10)**24)
R=6417*(10**3)
T=float(raw_input("enter whatever u want"))*3600
def satellite(T):
    h = (G*M*(T**2)/4/3.14/3.14)**(1.0/3)-R
    return h
print satellite(T) 

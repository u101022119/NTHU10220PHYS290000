
import math
def altitude(T):
       H=(-6743*10**3)+(((6.67*10**-11)*(5.97*10**24)*(T*T))/(4*math.pi**2))**(1/3)
       return H
print altitude(10000)

       

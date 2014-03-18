

# G*M*m/((h+R)**2)=m*4*(pi**2)*(R+h)/(T**2) => (h+R)**3=G*M*(T**2)/(4*(pi**2))
#=> h+R=(G*M*(T**2)/(4*(pi**2)))**(1/3) => h=(G*M*(T**2)/(4*(pi**2)))**(1/3)-R



import math


T=float(raw_input('enter the T you want : '))

print "the attitude is : ", (6.67*10**-11*5.97*10**24*T**2/4/math.pi**2)**(1.0/3)-6417000

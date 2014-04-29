import math 
T=input("enter the value of the period T(second):")
R=6417000.0         #單位:m
G=6.67 * 10 **(-11) #單位:m**3/(kg*s**2)
M=5.97 * 10 **24    #單位:kg
A=G * M * (T **2) /4.0/math.pi**2
h=A ** (1.0/3.0) - R

print "the attitude is",h,"meters"
      


   

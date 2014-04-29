# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 19:48:08 2014

@author: Sonic
"""

e=1.602*10**(-19)
a=564.02*10**-12
#e=1
#a=1
i=0
j=0
k=0

def v(i,j,k):
        
    x=1/(i**2+j**2+k**2)**(0.5)/4/3.14*e/a
    if (i+j+k)%2==0:
        return x
    else:
        return -x
        
def sumv(l):
    addsup=0
    i=-l
    j=-l
    k=-l
    while i<=l:
        while j<=l:        
            while k<=l:
                  addsup=addsup+v(i,j,k)
                  k=k+1
                  
            j=j+1
            
        i=i+1
    return addsup   

print v(1,0,0),v(2,0,0)
L=float(raw_input("Type L as limit here."))
print sumv(L)

#b=[]        
    
#t=0
#while t<3:
#    b.append(float(raw_input("Type in i,j,k, in order.")))
#    t=t+1""
    
#print v(b[0],b[1],b[2])   



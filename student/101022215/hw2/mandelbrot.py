# -*- coding: utf-8 -*-
"""
Created on Tue May 13 08:40:14 2014

@author: user
"""


 
import numpy as np

n=200
x=np.linspace(-2,2,n)
y=np.linspace(-2,2,n)
	
a=np.zeros(n**2)
b=np.zeros(n**2)
	
for i in range(n) :
    for j in range(n) :	   
        z=0+0j
        for k in range(100) :
            z=z**2+( x[i]+y[j]*1j )
            if z*z.conjugate()>4 :
                break
            elif k==99 :
              if  z*z.conjugate()<=4 :
                a[n*i+j]=x[i]
                b[n*i+j]=y[j]
	   
plot(a,b)
show()

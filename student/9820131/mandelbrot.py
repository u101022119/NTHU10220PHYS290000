# -*- coding: utf-8 -*-
"""
Created on Tue May 06 12:41:16 2014

@author: user2
"""
from pylab import*
x=linspace(-2,2,41)
y=linspace(-2,2,41)
i=0
j=0
k=0
for i in range(0,40):
    for n in range(0,40):    
        z1=0
        z2=0
        for k in range(0,999):
            x1=x.copy()
            y1=y.copy()
            if (z1**2+z2**2)<=4:                               
                z1=z1**2-z2**2+x1[i]
                z2=2*z1*z2+y1[n]
                k=k+1
        if (z1**2+z2**2)<=4:
            plot(x[i],y[n],'k.')
        else:
            plot(x[i],y[n],'w.')
        n=n+1
    i=i+1
show()

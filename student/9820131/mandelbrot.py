# -*- coding: utf-8 -*-
"""
Created on Tue May 06 12:41:16 2014

@author: user2
"""
from pylab import*
x=linspace(-2,2,11)
y=linspace(-2,2,11)
i=0
j=0
k=0
for i in range(0,10):
    for n in range(0,10):    
        c1=0
        c2=0
        for k in range(0,999):
            x1=x.copy()
            y1=y.copy()
            if x1[i]**2+y1[n]**2<=2:
                c1=c1+(x1[i])
                c2=c2+(y1[n])
                (x1[i])=x1[i]**2+y1[n]**2+c1
                y1[n]=y1[n]+c2
                k=k+1
        if x1[i]**2+y1[n]**2<=2:
            scatter(x[i],y[n],'black')
        else:
            scatter(x[i],y[n],'white')
        n=n+1
    i=i+1
xlim=(-10,10)
ylim=(-10,10)
show()

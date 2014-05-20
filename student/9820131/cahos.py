# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 16:45:25 2014

@author: user2
"""
from matplotlib.pylab import*
i=k=0
r=linspace(0,4,401)
x=zeros(1000)
x[0]=0.5
for k in range(0,400):
    for i in range(0,999):
        x[i+1]=r[k]*x[i]*(1-x[i])
        if i>950:
            plot(r[k],x[i],'b,')
        i=i+1
    k=k+1
show()


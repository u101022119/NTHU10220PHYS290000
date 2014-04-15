# -*- coding: utf-8 -*-
"""
Created on Tue Apr 08 09:36:42 2014

@author: user
"""
import numpy as np
from pylab import *
x=linspace(-2,2,N)
y=linspace(-2,2,N)
a=np.zeros(N*N)
b=np.zeros(N*N)
for i in range(N):
    for j in range(N):
        x0=0
        i0=0
        for k in range(100):
            x1=x0*x0-i0*i0+x[i]
            i1=2*x0*i0+y[j]
            x0=x1
            i0=i1
            if((x0*x0+i0*i0)>100):
                break
        if((x0*x0+i0*i0)<=4):
            a[N*i+j]=x[i]
            b[N*i+j]=y[j]
plot(a,b,'k.')
show()
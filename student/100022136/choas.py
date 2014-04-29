# -*- coding: utf-8 -*-
"""
Created on Tue Apr 08 09:02:54 2014

@author: user
"""
N=1001
import numpy as np
from pylab import *
r=linspace(1,4,N)
a=np.zeros(1000*N)
b=np.zeros(1000*N)
for i in range(N):
    x=0.5
    for j in range(1000):
        x=r[i]*x*(1-x)
    for k in range(1000):
        a[i*1000+k]=x
        x=r[i]*x*(1-x)
        b[i*1000+k]=r[i]
plot(b,a,'k.')
show()
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 15:58:59 2014

@author: user
"""

from pylab import *
import numpy as np

n = 200
x = np.linspace(-2,2,n)
y = np.linspace(-2,2,n)

a1 = np.zeros(n**2)
a2 = np.zeros(n**2)

for i in range(n):
    for j in range(n):
        z = 0 + 0j
        for k in range(100):
            z = z**2+(x[i]+y[j]*1j)
            if z*z.conjugate()>4:
                break            
        if z*z.conjugate()<=4:
            a1[n*i+j] = x[i]
            a2[n*i+j] = y[j]

plot(a1,a2,'k.')
show()
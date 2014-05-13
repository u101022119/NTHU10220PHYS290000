# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 23:12:19 2014

@author: larry lu
"""
from pylab import *
import numpy as np
n = 200
cr = np.linspace(-2,2,n)
ci = np.linspace(-2,2,n)
zr=0
zi=0
z=complex(zr,zi)
a1 = []
a2 = []
for i in range(n):
    for j in range(n):
        z = 0+0j
        for k in range(100):
            z=z**2+cr[i]+ci[j]*1j
            if z*z.conjugate()>4:
                break
        if z*z.conjugate()<=4:
            a1.append(cr[i])
            a2.append(ci[j])            
            
plot(a1,a2,'k.')
show()
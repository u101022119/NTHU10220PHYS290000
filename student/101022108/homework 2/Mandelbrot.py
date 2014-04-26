# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 13:35:00 2014

@author: Mark
"""

#from cmath import *
from pylab import *







x = arange(-2,2,0.01)
y = arange(-2,2,0.01)
creal = []
cimage = []
X1 = empty([len(x),len(y)],float)
for i in range(len(x)):
    for j in range(len(y)):
        c = complex(x[i],y[j])
        z = 0+0j
        for k in range(100):
            z=z**2+c
            if abs(z)>2:
                X1[j,i] = k
                break
            
        if abs(z)<=2:
            X1[j,i] = abs(z)*100
            creal.append(x[i])
            cimage.append(y[j])
            
            
#plot(creal,cimage,'k.')
imshow(X1,origin="lower",extent=[-2,2,-2,2])
jet()
show()
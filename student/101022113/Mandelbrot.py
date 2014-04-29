# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 22:20:52 2014

@author: Sonic
"""
from numpy import *
from pylab import *

z=0+0j
xlimit=arange(-2,2,0.01)
ylimit=arange(-2,2,0.01)
cr=[]
ci=[]
Z0=empty([len(xlimit),len(ylimit)],float)
for a in range(len(xlimit)):    
    for b in range(len(ylimit)):
        cx=complex(xlimit[a],ylimit[b])
        #print 'c',c
        
        for k in range(100):
            z=0+0j
            z=z**2+c
            if abs(z)>2:
                Z0[b,a] = k            
                break

        if abs(z)<=2:
            Z0[b,a]=abs(z)*100
            cr.append(xlimit[a])
            ci.append(ylimit[b])
            

#imshow(X,)
plot(cr,ci,'k.')
jet()
show()
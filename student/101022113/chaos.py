# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 22:03:47 2014

@author: Sonic
"""
from math import *
from pylab import *

def logisticmap(n,r):
    if n==0:
        return 0.5
    else:
            
        a=logisticmap(n-1,r)
        return r*a*(1-a)
      
r=arange(1,4,0.01)
x=logisticmap(100,r)

xlabel('r')
ylabel('x')
title('LogisticMap')
plot(r,x) 

show()   
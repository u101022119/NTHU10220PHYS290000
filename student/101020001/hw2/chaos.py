# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 09:17:07 2014

@author: user
"""

 ##Deterministic Chaos


from pylab import *
x = 0.5
r=arange(1,4,0.01)
for i in range(1000):
      x=r*x*(1-x)
      
plot(r,x)
show()

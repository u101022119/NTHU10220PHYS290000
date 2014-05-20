# -*- coding: utf-8 -*-
"""
Created on Mon May 19 00:23:53 2014


"""
from pylab import *

x=0.5
r=arange(1,4,0.001)
for i in range(1000):
    x=x*r*(1-x)
xlabel('r')
ylabel('x')
title('logistic map')
plot(r,x)
show()
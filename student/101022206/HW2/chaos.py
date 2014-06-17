# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 15:58:36 2014

@author: user
"""

from pylab import *


x = 0.5
r = arange(1,4,0.001)
for i in range(1000):
    x = r*x*(1-x)
xlabel('r')
ylabel('x')
title('logistic map')
    
plot(r,x)
show()
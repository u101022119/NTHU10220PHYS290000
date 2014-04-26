# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 12:12:00 2014

@author: Mark
"""

from math import *
from pylab import *

	
def LMap(n,r):
    if n==0:
        return 0.5
    else:
        k = LMap(n-1,r)
        return r*k*(1-k)
r = arange(1, 4, 0.01)
x = LMap(100,r)
xlabel('r')
ylabel('x')
title('logistic map')
plot(r,x)

show()


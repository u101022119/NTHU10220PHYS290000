# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 23:37:27 2014

@author: User
"""

from pylab import *

x = 0.5
r = arange(1, 4, 0.01)
for i in range(1000):
    x = r*x*(1-x)
title('Logistic Map')
plot(r, x)

show()
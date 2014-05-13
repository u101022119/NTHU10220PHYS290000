# -*- coding: utf-8 -*-
"""
Created on Tue May 13 00:19:34 2014

@author: Administrator
"""
from matplotlib.pylab import *
def f(t):
    return t**2*exp(-t**2)
t = linspace(0, 3, 51)
y = f(t)
plot(t, y)
show()
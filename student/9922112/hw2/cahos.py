# -*- coding: utf-8 -*-
"""
Created on Tue May 13 13:06:45 2014

@author: Administrator
"""

from matplotlib.pylab import *

def log(r,x,n):   #start from x, growth rate r, do n times
    k=1
    while k<n:
        x=r*x*(1-x)
        k=k+1
    return x
from matplotlib.pylab import *
r = arange(1,3,0.01)
y = log(r,2,100)
plot(r,y)
show()
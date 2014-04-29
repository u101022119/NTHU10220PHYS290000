# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 16:59:26 2014

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt


rnum=1000
r=linspace(1,4,rnum)
x=ones(rnum)/2.0

def rec(arg):
    for i in range(rnum):
        x[i]=r[i]*x[i]*(1-x[i])
    plt.plot(r,x,arg)
        
        
for i in range(300):
    rec('r,')
for i in range(100):
    rec('b,')


plt.show()
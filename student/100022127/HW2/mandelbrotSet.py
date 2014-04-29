# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 16:59:26 2014

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt


num=100
cx=linspace(-2,2,num)
cy=linspace(-2,2,num)
z=zeros(num**2)+0j

def rec(time,arg):
    for j in range(time):
        for x in range(num):
            for y in range(num):
                z[x*num+y]=z[x*num+y]**2+(cx[x]+cy[y]*1j)
    for x in range(num):
        for y in range(num):
            if z[x*num+y]<=2:
                plt.plot(cx[x],cy[y],arg)
        
        
rec(20,'r.')
rec(40,'g.')
rec(40,'b.')


plt.show()
# -*- coding: utf-8 -*-
"""
Created on Thu May 01 13:17:59 2014

@author: Administrator
"""

L = 1000
r = 1
xlist = []
rlist = []

while r <= 4:
    rlist.append(r)
    x = 0.5
    n = 0
    while n < L:
        x = r * x * (1-x)
        n += 1
    xlist.append(x)
    r = r + 0.01

print xlist

import matplotlib.pyplot as plt

plt.figure()
plt.plot(rlist,xlist)
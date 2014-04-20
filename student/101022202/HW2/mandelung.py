# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Gary\.spyder2\.temp.py
"""
import numpy as np
import matplotlib.pyplot as plt
def f1(t):
    return t**2*np.exp(-t**2)
def f2(t):
    return t**2*f1(t)
t = np.linspace(0,3,51)
y1 = f1(t)
y2 = f2(t)
plt.plot(t,y1,'r-')
plt.plot(t,y2,'bo')
plt.xlabel('t')
plt.ylabel('y')
plt.show()

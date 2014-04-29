# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 16:35:34 2014

@author: user
"""


mL=301
a=ones(mL**2*3)*(-1)

def rms(x,y,z):
    i=x**2+y**2+z**2
    if a[i]==-1.0:
        a[i]=1.0/(i)**0.5*(-1)**(x+y+z)
    return a[i]

ML=[]
Vt=0.0
for L in range(mL)[1:]:
    M=0.0
    for x in range(L)[1:]:
        for y in range (L)+[L]:
            M+=rms(x,y,L)
    M=M*4+rms(L,L,0)*2+rms(L,0,0)
    M=M*6
    M=M+8*rms(L,L,L)
    Vt+=M
    if(L%15==0):
        print "Vt(",L,") = ",Vt," M= ",M
    ML.append(Vt)

import numpy as np
import matplotlib.pyplot as plt
plt.plot(range(mL)[1:],ML,"r-")
plt.show()

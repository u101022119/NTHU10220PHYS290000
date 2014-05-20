# -*- coding: utf-8 -*-
"""
Created on Fri May 02 15:57:24 2014

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

# show the z serials
'''
def Polynomial(n,c):
    if n == 0:
        print 'z(n+1) = z(n)^2 + c, and c =',c
        print 'z0 =', 0
        return 0
    else:
        z = Polynomial(n-1,c) ** 2 + c
        print 'z%d =' % n, z
        return z
'''

N = 500+1
creal = np.linspace(-2.0,2.0,N)
cimage = np.copy(creal)
M = np.zeros(N**2).reshape(N,N) #empty([N,N],float)
Mx = []
My = []

for i in range(N):
    for j in range(N):
        
        c = complex(creal[i],cimage[j])
        z = 0+0j
        n = 0
        while abs(z) <= 2 :
            z = z ** 2 + c
            n += 1
            if n > 100:
                break
                
        if abs(z) > 2 :
            M[j,i] = n
        else: #abs(z) <= 2
            M[j,i] = abs(z)
            Mx.append(creal[i])
            My.append(cimage[j])
            
plt.figure(0)
plt.plot(Mx, My, 'k.')
plt.axis([-2.0, 2.0, -2.0, 2.0])

plt.figure(1)
plt.imshow(M, origin = 'lower', extent=[-2,2,-2,2])
plt.jet()
plt.show()
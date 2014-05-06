# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 16:43:13 2014

@author: user2
"""
L=100
i=j=k=-L
V=0
for i in range(-L,L):
    for j in range(-L,L):
        for k in range(-L,L):
            if i**2+j**2+k**2!=0:
                V=V+(-1)**(i+k+j)*((i**2+j**2+k**2)**(-0.5))
            k=k+1
        j=j+1
    i=i+1
print V

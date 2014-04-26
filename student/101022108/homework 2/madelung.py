# -*- coding: utf-8 -*-
"""
Created on dThu Apr 24 15:56:40 2014

@author: Mark
"""

import math


def V(i,j,k):
    if i==0 and j==0 and k==0:
        return 0
    elif (i+j+k)%2==0:
        return (i**2+j**2+k**2)**-0.5
    elif (i+j+k)%2==1:
        return -((i**2+j**2+k**2)**-0.5)
    
L = int(raw_input('Input L :\n'))
i = -L
j = -L
k = -L
summary = 0.0

while i<=L:
    while j<=L:
        while k<=L:
            summary = summary + V(i,j,k)
            k=k+1
        k=-L
        j=j+1
    j=-L
    i=i+1
print summary
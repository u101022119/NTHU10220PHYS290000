# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 00:03:35 2014

@author: User
"""

import math

L = int(raw_input("Enter the value of L:"))

i = -L
j = -L
k = -L

M = 0

while i <= L:
    while j <= L:
        while k <= L:
            if i == 0 and j == 0 and k == 0:
                M = M
            elif (i+j+k)%2 == 0:
                 M = M +(i**2+j**2+k**2)**(-0.5)
            else :
                 M = M -(i**2+j**2+k**2)**(-0.5)
            k = k+1
        j = j+1
        k = -L
    i = i+1
    j = -L
    
print M

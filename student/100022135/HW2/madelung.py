# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 17:36:15 2014

@author: user
"""
import math

L=50

i=-L
j=-L
k=-L

M=0

while i<=L:
    while j<=L:
        while k<=L:
            if i==j & j==k & k==0 :
                M=M
            elif (i+j+k )%2==0:
                M=M+(i**2+j**2+k**2)**(-1.0/2.0)
            else: 
                M=M-(i**2+j**2+k**2)**(-1.0/2.0)                                      
            k=k+1            
        j=j+1
        k=-L
    i=i+1
    j=-L

print M

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 16:44:44 2014

@author: user2
"""

i=2
while (i <=10000):
    j=2
    P=0
    while (j<=i**0.5):
        if (i)%(j)==0:
            P=P+1
            j=j+1
        else:
            P=P
            j=j+1
    if P==0:
        print i
    i=i+1

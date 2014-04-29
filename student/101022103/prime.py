# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 17:26:50 2014

@author: user
"""
from numpy import *

primelist = [2]

i = 2

while i<=100:
    count = 0
    j=0
    while j <= len(primelist)-1:
        if i % primelist[j] == 0:
            count = count+1
        j = j+1
    if count == 0:
        primelist.append(i)
    i+=1

print primelist
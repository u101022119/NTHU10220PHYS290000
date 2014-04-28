# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 21:37:02 2014

@author: Mark
"""
import math

primelist = [2]
n=3
count=0
i=0

while n<=10000:
    while primelist[i]<=int(math.sqrt(n)):
        if n%primelist[i]==0:
                count+=1
        i+=1
    if count==0:
        primelist.append(n)
    n=n+1
    i=0
    count=0

print primelist
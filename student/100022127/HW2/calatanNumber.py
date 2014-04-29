# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\user\.spyder2\.temp.py
"""

c=1
n=0
while c < 1000000:
    print c,
    c=(4*n+2)*c/(n+2)
    n=n+1
   # if n % 10 == 0:
    #    print ' '

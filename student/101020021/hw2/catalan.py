# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\user\.spyder2\.temp.py
"""

def cccc(n):
    if n<0:
        return none
    if n==0:
        return 1
    if n>0:
        return (4*n+2)/(n+2)*cccc(n-1)
    
n=0

while 1:
    print 'for n = ',n,' , Cn = ',cccc(n)
    
    if cccc(n+1)>10**9:
        break
    n=n+1
    
# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\user\.spyder2\.temp.py
"""

def prime(n):
    if n == 2:
        print n,
    else:
        a = int(n**0.5)   
        b = range(a+2)
        k = 0
        for i in b[2:]:
            if float(n)/i - int(n/i) == 0:
                k = k+1
             
        if k == 0:
            print n,

a = range(999999)

for i in a[2:]:
    prime(i)

        
        
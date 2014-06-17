# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 15:59:55 2014

@author: user
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
b = int(raw_input('Put an integer:'))
a = range(b+1)

for i in a[2:]:
    prime(i)
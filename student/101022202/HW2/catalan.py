# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\user\.spyder2\.temp.py
"""

def prime(n):
    a = int(n**0.5)
    b = range(a+1)
    k = 0
    for i in b[2:]:
        if float(n/i) - int(n/i) == 0:
            k = k+1
    if k == 0:
        print n
                
prime(23)

        
        
# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\user\.spyder2\.temp.py
"""

def catalan(n):
    if n == 0:
        return 1
    else:
        a = float(((4.0*n-2)/(n+1))) * float(catalan(n-1))
        return a
        
print catalan(6)
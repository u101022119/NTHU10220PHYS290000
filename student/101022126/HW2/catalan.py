# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Administrator\.spyder2\.temp.py
"""

def catalan(m):
    c = 1.0
    n = 0
    
    while c <= m:
        print 'C%d =' % n ,c
        c = (4.0*n + 2) / (n + 2) * c
        n += 1

catalan(1000000000)
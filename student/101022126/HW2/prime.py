# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 13:56:10 2014

@author: Administrator
"""

def find_prime(m):
    primelist = [2]
    n = 1
    p = 3
    while p <= m:
        t = len(primelist)
        for pi in range(t):
            if p % primelist[pi] == 0:
                break
            elif p % primelist[pi] != 0 and pi == t-1:
                primelist.append(p)
        
        n += 1
        p = 2*n + 1
        
    print primelist

find_prime(10000)
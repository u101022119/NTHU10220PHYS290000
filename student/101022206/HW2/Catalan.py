# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 17:03:51 2014

@author: user
"""

def catalan(n):
    if n==0:
        return 1
    else:
        return (4*n-2)*catalan(n-1)/(n+1)

n=0
while catalan(n)<1000000:
    print catalan(n)
    n=n+1


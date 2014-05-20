# -*- coding: utf-8 -*-
"""
Created on Tue May 20 17:00:20 2014

@author: user
"""

def prime(k):
    if k==2:
        print k,
    else:
        a=int(k**0.5)
        b=range(a+2)
        n=0
        for i in b[2:]:
            if float(k)/i - int(k/i) ==0:
                n=n+1

        if n==0:
            print k,
b=int(raw_input('Put an interger:'))
a=range(b+1)

for i in a[2:]:
    prime(i)

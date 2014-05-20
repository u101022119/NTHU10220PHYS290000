# -*- coding: utf-8 -*-
"""
Created on Mon May 12 10:46:14 2014

@author: Administrator
"""
def ack(m,n):
    if m<0 or n<0:
        print'm,n must be interger>=0'
    elif m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    else:
        return ack(m-1,ack(m,n-1))
print ack(3,4)

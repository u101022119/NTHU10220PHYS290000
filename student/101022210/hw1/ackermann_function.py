# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 23:06:51 2014


"""
m=int(raw_input('please input m:'))
n=int(raw_input('please input n:'))

def ackermann(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ackermann(m-1,1)
    elif m>0 and n>0:
        return ackermann(m-1,ackermann(m,n-1))
ack=ackermann(m,n)
print 'the result is:',ack
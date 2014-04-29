# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 16:59:26 2014

@author: user
"""

def random_list(N,a,b):
    ret=zeros(N)
    for i in range(N):
        ret[i]=randint(a,b)
    return ret

def quick_rec(A,B,min,max):
    if(max-min<=0):
        return A;
    n=A[min]
    a=min
    b=max-1
    for i in range(max)[min+1:]:
        if A[i]<n:
            B[a]=A[i]
            a=a+1
        else:
            B[b]=A[i]
            b=b-1
    if a!=b:
        print "error!  a!=b ",a,b
    B[a]=n
    print A
    print B,min,max
    rA=quick_rec(B,A,min,a)
    rB=quick_rec(B,A,a+1,max)
    if rA is not rB:
        for i in range(max)[a+1:]:
            rA[i]=rB[i]
    return rA
    
        
def quick_sort(list):
    temp=zeros(size(list))
    print sorted(list)
    quick_rec(list,temp,0,size(list))
    print list
    print temp

r=random_list(10,100,500)
print r
print quick_sort(r)


import numpy as np
import matplotlib.pyplot as plt

num=100
cx=linspace(-2,2,num)
cy=linspace(-2,2,num)
z=zeros(num**2)+0j

#plt.plot(cx[x],cy[y],'r-')
#plt.show()
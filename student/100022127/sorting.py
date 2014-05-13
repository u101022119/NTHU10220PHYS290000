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

def swap(list,a,b):
    temp=list[a]
    list[a]=list[b]
    list[b]=temp

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
    A[a]=n
    quick_rec(B,A,min,a)
    quick_rec(B,A,a+1,max)
        
def quick_sort(list):
    temp=zeros(size(list))
    quick_rec(list,temp,0,size(list))
    return list

def selection_sort(list):
    for i in range(size(list)):
        min=i
        for j in range(size(list))[i+1:]:
            if list[j]<list[min]:
                min=j
        swap(list,i,min)
    return list

def bubble_sort(list):
    for i in range(size(list)):
        for j in range(size(list)-i-1):
            if list[j]>list[j+1]:
                swap(list,j,j+1)
    return list

def insertion_sort(list):
    for i in range(size(list))[1:]:
        n=list[i]
        j=i-1
        while list[j]>n and j>=0:
            list[j+1]=list[j]
            j=j-1
        list[j+1]=n
    return list

r=random_list(12,10,90)
print r,
print sorted(r)
q=r.copy()
print q,
print quick_sort(q)
s=r.copy()
print s,
print selection_sort(s)
b=r.copy()
print b,
print bubble_sort(b)
i=r.copy()
print i,
print insertion_sort(i)

import numpy as np
import matplotlib.pyplot as plt
import time

x=[2,4,6,8,10,20,50,100,300,1000,3000]
ra=[]
for i in x:
    ra.append(list(random_list(i,10,100000)))

def plotSort(sort,arg):
    ret=[]
    for i in range(size(x)):
        fin=array(ra[i]).copy()
        t0=time.clock()
        sort(fin)
        t1=time.clock()
        ret=ret+[np.log(t1-t0)]
    plt.plot(range(size(x)),ret,arg)


plotSort(quick_sort,'r-')
plotSort(bubble_sort,'g-')
plotSort(selection_sort,'b-')
plotSort(insertion_sort,'y-')
plotSort(sorted,'k-')
plt.show()

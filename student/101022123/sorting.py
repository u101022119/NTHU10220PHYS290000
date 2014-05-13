# -*- coding: utf-8 -*-
"""
Created on Tue May 13 16:42:59 2014

@author: user
"""
import random
l = []
temp =[]

def random_list(N,a,b):
    for i in range (N):
        l.append(random.randint(a,b))
        return l
    
def selection_sort(l):
    print random.sample(l,N)

def insertion_sort(l,N):
    for i in range (N):
        l.append(random.randint(a,b))
        print l

def bubble_sort(l):
    for j in range (len(l)):
        for i in range (len(l)-1):
            if l[i]<l[i+1]:
                temp=l[i]
                l[i]=l[i+1]
                l[i+1]=temp

a=1
b=100
N=5
random_list(N,a,b)

insertion_sort(l,N)
print l

bubble_sort(l)
print l    
    
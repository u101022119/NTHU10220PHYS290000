# -*- coding: utf-8 -*-
"""
Created on Tue May 13 04:32:40 2014

@author: user
"""

import random

def random_list(N,a,b):
    c=[]
    for i in range(N):
        c.append(random.randint(a,b))
    return c
print random_list(1,1,100)

def selection_sort(c,N):
    print random.sample(c,N)

print selection_sort([1,2,3,4,5,6,7,8,9],5)

def insertion_sort(c,N):
    for i in range(N):
        c.append(random.randint(a,b))
        print c
a=0
b=100        
def bubble_sort(c):
    for i in range(len(c)):
        for j in range(len(c)-1):
            if c[j] < c[j+1]:
                temp = c[j]
                c[j] = c[j+1]
                c[j+1] = temp
    print c

insertion_sort(random_list(5,0,100),10)
bubble_sort(random_list(5,0,100))

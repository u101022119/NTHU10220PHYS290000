# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 15:08:36 2014


"""

import random
def random_list(N,a,b):
    k=[]
    for i in range(N):
        k.append(random.randint(a,b))
    return k

def selection_sort(k,N):
    print random.sample(k,N)

def insertion_sort(k,N):
    for i in range(N):
        k.append(random.randint(a,b))
    print k
def bubble_sort(k):
    for i in range(len(k)):
        for j in range(len(k)-1):
            if k[j] < k[j+1]:
                temp = k[j]
                k[j] = k[j+1]
                k[j+1] = temp
    print k

a = 0
b = 100
insertion_sort(random_list(6,0,100),10)
bubble_sort(random_list(6,0,100))

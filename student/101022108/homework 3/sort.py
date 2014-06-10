# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 15:46:52 2014

@author: Mark
"""
sys.setrecursionlimit(10000)
from random import *
from numpy import *
from matplotlib.pylab import *
import time


def random_list(N, a, b):
    k = []
    i = 0
    while i<N:
        k.append(randint(a, b))
        i+=1
    
    return k


def selection_sort(s):
    for i in range(len(s)):
        min = s[i]
        temp = i
        for k in range(i, len(s)):
            if s[k] < min:
                min = s[k]
                temp = k
        s[i], s[temp] = s[temp], s[i]
    return s
    
def insertion_sort(s):
    temp = []
    temp.append(s[0])
    for i in range(1, len(s)):
        for j in range(len(temp)):
            if s[i] < temp[j]:
                temp[j:j] = [s[i]]
                break
            if s[i] >= temp[len(temp)-1]:
                temp.append(s[i])
                break
    return temp
    
def bubble_sort(s):
    while True:
        count = 0
        for i in range(len(s)-1):
            if s[i+1]<s[i]:
                s[i], s[i+1] = s[i+1], s[i]
                count+=1
        if count == 0:
            return s            
            break

def qsort(s, left, right):
    pivot = s[right]
    ln = left
    rn = right
    if ln == rn: 
        return s
    while True:
        while s[ln] <= pivot and rn > ln:
            ln+=1
        while s[rn] >= pivot and rn > ln:
            rn-=1
        s[ln], s[rn] = s[rn], s[ln]
        if ln >= rn :
            break
    s[rn] , s[right] = s[right] ,s[rn]
    if left < ln:
        qsort(s, left, ln-1)
    qsort(s, rn, right)

def quick_sort(s):
     right = len(s)-1
     left = 0
     qsort(s, left, right)
     return s

def time_spend(f, s):
    start = time.time()
    f(s)
    end = time.time()
    return end - start
  
x = zeros(len(range(100,5000,100)))
y1 = zeros(len(range(100,5000,100)))
y2 = zeros(len(range(100,5000,100)))
y3 = zeros(len(range(100,5000,100)))
y4 = zeros(len(range(100,5000,100)))
y5 = zeros(len(range(100,5000,100)))
k = 0

for elements in range(100, 5000, 100):
    s = random_list(elements, 0, 10000)
    x[k] = elements
    y1[k] = time_spend(selection_sort, s)
    y2[k] = time_spend(insertion_sort, s)
    y3[k] = time_spend(bubble_sort, s)
    y4[k] = time_spend(quick_sort, s)
    y5[k] = time_spend(sorted, s)
    k+=1

xlabel ('elements')
ylabel ('time spent')
plot(x, y1)
plot(x, y2)
plot(x ,y3)
plot(x ,y4)
legend(['selecion', 'insertion', 'bubble','quick', 'sorted'])
show()
'''loglog(x, y5)
loglog(x, y1)
loglog(x, y2)
loglog(x ,y3)
loglog(x ,y4)
loglog(x, y5)
legend(['selecion', 'insertion', 'bubble','quick', 'sorted'])
show()
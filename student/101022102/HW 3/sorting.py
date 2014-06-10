# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 15:45:23 2014

@author: user
"""

from random import *
from time import time
from pylab import *

def random_list(N):
    array=[]
    for i in range (0,N):
        array.append(randint(0,N-1))
    return array
    
def selection_sort(array):
    for i in range (0,len(array)):
        min = i
        for j in range(i+1,len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
        
def insertion_sort(array):
    for i in range(1,len(array)):
        save = array[i]
        j = i
        while j > 0 and array[j-1] > save:
            array[j] = array[j-1]
            j -= 1
        array[j] = save
        
def bubble_sort(array):
    done = False
    while not done:
        done = True
        for i in range(len(array)-1,0,-1):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
                done = False

def quick_sort_list(array):
    if array == []:
        return []
    else:
        pivot = array[0]
        lesser = quick_sort_list([x for x in array[1:] if x < pivot])
        greater = quick_sort_list([x for x in array[1:] if x >= pivot])
        return lesser+[pivot]+greater

    
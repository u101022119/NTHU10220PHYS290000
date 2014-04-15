"""
Title:   exercise in the class
#Due:    4/22/2014
#Author: 101022171, chin-hua Cheng
"""
import random
from numpy import * 

#assign random integers from 0 to 1000 to the a array
def random_array():
    for i in range(0,10):
        a[i] = random.randint(0, 100)


def selection_sort(a):
    for j in range(0,9):
    
        imin = j
    
        for i in range(j+1, 10):
            if a[i] < a[imin]:
                imin = i
    
        if imin != j :
            t = a[j]
            a[j] = a[imin]
            a[imin] = t


a = zeros(10, int) #declare an array which is 10 of size
random_array()

print "array", a
selection_sort(a)
print "after selection sort:"
print "array", a
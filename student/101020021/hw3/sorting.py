# -*- coding: utf-8 -*-
"""
Created on Tue May 20 16:38:35 2014

@author: user
"""

import random

def random_list(N,a,b):
    lst=[]
    for i in range(N):
        lst.append(randint(a,b))
    return lst


def selection_sort(lst):
    for i in range(len(lst)):
        min_o=i
        for j in range(i,len(lst)):
            if lst[j]<lst[min_o]:
                min_o=j
            
        a=lst[i]
        lst[i]=lst[min_o]
        lst[min_o]=a
    
    
def insertion_sort(lst):
    for i in range(len(lst)):
        for j in range(i):
            if lst[0]>lst[i]:
                a=lst[i]
                for k in range(i-1):
                    lst[i-k]=lst[i-k-1]
                lst[0]=a
                break                
            elif lst[j]<=lst[i] and lst[j+1]>=lst[i]:
                a=lst[i]
                for k in range(i-j-1):
                    lst[i-k]=lst[i-k-1]
                lst[j+1]=a
                break
            
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j]>lst[j+1]:
                a=lst[j+1]
                lst[j+1]=lst[j]
                lst[j]=a
    
    
def quick_sort(lst):
    c=0
    for i in range(len(lst)):
        b=0
        for j in range(len(lst)-i-1):
            if lst[j]>lst[-i-1]:
                a=lst[j]
                lst[j]=lst[-i-2]
                lst[-i-2]=lst[-i-1]
                lst[-i-1]=a
                break
            elif j==len(lst)-i-2:
                b=1
                c=j+1                
        if b:
            break
    quick_sort(lst[:c+1])
    quick_sort(lst[3+c:])
    
lst=random_list(10,0,10)
print lst
quick_sort(lst)
print lst
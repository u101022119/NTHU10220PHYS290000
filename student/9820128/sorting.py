# -*- coding: utf-8 -*-
"""
Created on Tue May 13 15:30:57 2014

@author: user
"""


def find_smallest(x): 
    if len(x)>1: 
        r=[] 
        for s in range(0,len(x),2): 
            if s==len(x)-1: 
                r.append(x[s]) 
            elif x[s]>x[s+1]: 
                r.append(x[s+1]) 
            else: 
                r.append(x[s]) 
        x=r 
        return find_smallest(r) 
    return x[0]         
    
def random_list(N,a,b):
    t=[]
    for i in range(N):
        s = randint(a,b)
        t.append(s)
    return t

def selection_sort(x):
    t=[]
    for i in range(len(x)):
        s=find_smallest(x)
        t.append(s)
        x.remove(s)
    return t
    
def insertion_sort(x):
    t=[]
    while len(x) > 0:
        if len(t)==0:
            t.append(x[0])
            x.pop(0)
        else:
            for i in range(len(x)):
                for j in range(len(t)):
                    if t[j]>x[i]:
                        s=[x[i]].extend(t)
                        x.pop(i)
                    
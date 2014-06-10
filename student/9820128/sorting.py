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
    print x
    t=[]
    t.append(x[0])
    x.pop(0)
    i=0
    while len(x)>0:
        if i+1<len(t) and t[i]<=x[0] and x[0]<t[i+1]:
            s=[x[0]]
            x.pop(0)
            s1=t[:i+1]
            s1.extend(s)
            s2=t[i+1:]
            s1.extend(s2)
            t=s1
            i=0
            print t,x
        elif x[0]<t[0]:
            s=[x[0]]
            x.pop(0)
            s.extend(t)
            t=s
            i=0
            print t,x
        elif x[0]>t[len(t)-1]:
            t.append(x[0])
            x.pop(0)
            i=0
            print t,x
        else:
            i+=1
    return t
    
def insertion_sort1(x):    #another way to do it
    t=[]
    t.append(x[0])
    x.pop(0)
    while len(x)>0:
        for i in range(len(t)):
            if i+1<len(t) and t[i]<=x[0] and x[0]<t[i+1]:
                s=[x[0]]
                x.pop(0)
                s1=t[:i+1]
                s1.extend(s)
                s2=t[i+1:]
                s1.extend(s2)
                t=s1
                break
            elif x[0]<t[0]:
                s=[x[0]]
                x.pop(0)
                s.extend(t)
                t=s
                break
            elif x[0]>t[len(t)-1]:
                t.append(x[0])
                x.pop(0)
                break
    return t
    
def bubble_sort(x):
    t=x[:]
    i=len(x)-1
    while i>0:
        if x[i]>=x[i-1]:
            i+=-1
        elif x[i]<x[i-1]:
            s=x[i]
            x[i]=x[i-1]
            x[i-1]=s
    if t==x:
        return x
    else:
        return bubble_sort(x)

def quick_sort(x):
    s=randint(0,len(x)-1)
    m=[]
    p=[]
    q=[]
    for i in range(len(x)):
        if x[i]<x[s]:
            m.append(x[i])
        elif x[i]==x[s]:
            p.append(x[i])
        else:
            q.append(x[i])
            print 'q1',q
    while len(m)>1:
        quick_sort(m)
        m=quick_sort(m)
        break
    while len(q)>1:
        quick_sort(q)
        q=quick_sort(q)
        break
    m.extend(p)
    m.extend(q)
    x=m
    return x
    
    
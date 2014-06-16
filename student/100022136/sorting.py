import random
import copy
import time, itertools

def random_list(N,a,b):
    li=[]
    for i in range(N):
        li.append(min(a,b)+int((abs(a-b)+1)*random.random()))
    return li
test=random_list(20,1,100)
print test

uso =[]

def selection_sort(a):
    so=[]
    uso=copy.copy(a)
    for i in range(len(a)):
        m = min(uso)
        so.append(m)
        uso.remove(m)
    return so
print 'selection:'
sel_start = time.time()
ls=selection_sort(test)
sel_stop = time.time()
st=sel_stop-sel_start
print ls
print st

def insertion_sort(a):
    so=[]
    for i in a:
        k=0
        for j in so:
            if i<j:
                so.insert(k,i)
                break
            k+=1
        if k == len(so):
                so.insert(k,i)
    return so
print 'insertion:'
ins_start = time.time()
lin= insertion_sort(test)
ins_stop = time.time()
it=ins_stop-ins_start
print lin
print it

def bubble_sort(a):
    uso=copy.copy(a)
    l = len(a)
    for i in range(l):
        for j in range(l-i-1):
            if uso[j]>uso[j+1]:
                uso[j],uso[j+1]=uso[j+1],uso[j]
    return uso
print 'bubble:'
bub_start = time.time()
lb=bubble_sort(test)
bub_stop = time.time()
bt=bub_stop-bub_start
print lb
print bt

def quick_sort(a):
    uso=[copy.copy(a)]
    l=len(a)
    so=[]
    while(len(uso)!=l):
        for i in uso:
            if len(i)!=1:
                n=i[0]
                lower=[]
                higher=[]
                for j in i[1:]:
                    if j<=n:
                        lower.append(j)
                    else:
                        higher.append(j)
                t=uso.index(i)
                uso.pop(t)
                if len(higher)!=0:
                    uso.insert(t,higher)
                uso.insert(t,[n])
                if len(lower)!=0:
                    uso.insert(t,lower)
                break
    for j in uso:
        so.append(j[0])
    return(so)
print 'quick:'
qui_sta=time.time()
lq=quick_sort(test)
qui_sto=time.time()
qt=qui_sto-qui_sta
print lq
print qt
print'sort:'
print sorted(test)



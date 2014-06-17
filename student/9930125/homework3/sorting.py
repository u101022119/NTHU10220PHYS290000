from random import randint
import time
import copy
import numpy as np
from pylab import *

def random_list(N,a,b):
    lst=[]
    for i in range(N):
        lst.append(randint(a,b))
    return lst


def selection_sort(lst):
    begin=time.time()
    for i in range(len(lst)):
        min_o=i
        for j in range(i,len(lst)):
            if lst[j]<lst[min_o]:
                min_o=j
            
        a=lst[i]
        lst[i]=lst[min_o]
        lst[min_o]=a
    end=time.time()
    return lst,(end-begin)
    
    
def insertion_sort(lst):
    begin=time.time()
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
    end=time.time()
    return lst,(end-begin)
            
def bubble_sort(lst):
    begin=time.time()
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j]>lst[j+1]:
                a=lst[j+1]
                lst[j+1]=lst[j]
                lst[j]=a
    end=time.time()
    return lst,(end-begin)
    
    
def quick_sort(lst):
    begin=time.time()
    c=0
    for i in range(len(lst)):
        b=0
        for j in range(len(lst)-i-1):
            if j==len(lst)-i-2:
                b=1
                c=j
            if lst[j]>lst[-i-1]:
                a=lst[j]
                lst[j]=lst[-i-2]
                lst[-i-2]=lst[-i-1]
                lst[-i-1]=a
                c=j-1
                break
        if b and ( 0<c ):
            lst[:c+1]=quick_sort(lst[:c+1])
        if b and ( c<(len(lst)-3) ):
            lst[2+c:]=quick_sort(lst[2+c:])
        if b:
            break
    end=time.time()
    return lst,(end-begin)



def build_in_sorted(lst):
    begin=time.time()
    sorted(lst)
    end=time.time()
    return lst,(end-begin)


N=200

x = arange(0,N,1)
y_1 = np.zeros(N)
y_2 = np.zeros(N)
y_3 = np.zeros(N)
y_4 = np.zeros(N)
y_5 = np.zeros(N)
a=[]
b=[]
c=[]
d=[]
e=[]
lst=[]

for i in arange(1,N):
    lst=random_list(i,0,100)
    a=lst[:]
    b=lst[:]
    c=lst[:]
    d=lst[:]
    e=lst[:]
    a,y_1[i]=selection_sort(a)
    b,y_2[i]=insertion_sort(b)
    c,y_3[i]=bubble_sort(c)
    d,y_4[i]=quick_sort(d)
    e,y_5[i]=build_in_sorted(e)

xlabel ('size')
ylabel ('time')
plot(x,y_1)
plot(x,y_2)
plot(x,y_3)
plot(x,y_4)
plot(x,y_5)

legend(['selecion', 'insertion', 'bubble','quick', 'build_in'])
show()


from random import randint
import time
import copy
import numpy as np
from pylab import *

def random_list(N,a,b):
    integer=[]
    for i in range(N):
        integer.append(randint(a,b))
    return integer


def selection_sort(integer):
    begin=time.time()
    for i in range(len(integer)):
        min_o=i
        for j in range(i,len(integer)):
            if integer[j]<integer[min_o]:
                min_o=j
            
        a=integer[i]
        integer[i]=integer[min_o]
        integer[min_o]=a
    end=time.time()
    return integer,(end-begin)
    
    
def insertion_sort(integer):
    begin=time.time()
    for i in range(len(integer)):
        for j in range(i):
            if integer[0]>integer[i]:
                a=integer[i]
                for k in range(i-1):
                    integer[i-k]=integer[i-k-1]
                integer[0]=a
                break                
            elif integer[j]<=integer[i] and integer[j+1]>=integer[i]:
                a=integer[i]
                for k in range(i-j-1):
                    integer[i-k]=integer[i-k-1]
                integer[j+1]=a
                break
    end=time.time()
    return integer,(end-begin)
            
def bubble_sort(integer):
    begin=time.time()
    for i in range(len(integer)):
        for j in range(len(integer)-i-1):
            if integer[j]>integer[j+1]:
                a=integer[j+1]
                integer[j+1]=integer[j]
                integer[j]=a
    end=time.time()
    return integer,(end-begin)
    
    
def quick_sort(integer):
    begin=time.time()
    c=0
    for i in range(len(integer)):
        b=0
        for j in range(len(integer)-i-1):
            if j==len(integer)-i-2:
                b=1
                c=j
            if integer[j]>integer[-i-1]:
                a=integer[j]
                integer[j]=integer[-i-2]
                integer[-i-2]=integer[-i-1]
                integer[-i-1]=a
                c=j-1
                break
        if b and ( 0<c ):
            integer[:c+1]=quick_sort(integer[:c+1])
        if b and ( c<(len(integer)-3) ):
            integer[2+c:]=quick_sort(integer[2+c:])
        if b:
            break
    end=time.time()
    return integer,(end-begin)



def build_in_sorted(integer):
    begin=time.time()
    sorted(integer)
    end=time.time()
    return integer,(end-begin)


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
integer=[]

for i in arange(1,N):
    integer=random_list(i,0,100)
    a=integer[:]
    b=integer[:]
    c=integer[:]
    d=integer[:]
    e=integer[:]
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

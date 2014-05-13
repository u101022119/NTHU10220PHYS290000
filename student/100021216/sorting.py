import random
import copy

l=[]

def list_swap(l,a,b):
    l[a],l[b]=l[b],l[a]

def random_list(N,a,b):
    for i in range(N):
        r=random.randint(a,b)
        l.append(r)
    return l


def selction_sort(l):
    for j in range(len(l)):
        imin=j
        for i in range(j,len(l)):
            if l[i]<l[imin]:
                imin=i         
        if l[imin]!=l[j]:
            list_swap(l,imin,j)


def insertion_sort(l):
    for i in range(1,len(l)):
        j=i
        while j>0 and l[j-1]>l[j]:
            list_swap(l,j - 1,j)
            j-=1


def bubble_sort(l):
    for i in range(0,len(l)):
        for j in range(1,len(l)-i):
            if l[j]<l[j-1]:
                list_swap(l,j - 1,j)

import time, itertools
from random import *
from matplotlib.pyplot import *

def random_list(N,a,b):
    return [randint(a,b) for x in range(N)]

L = range(10,1001,10)
def myTest(fun):
    dT = []
    for x in L:
        A = random_list(x,0,10)
        tStart = time.time()
        fun(A)
        tStop = time.time()
        dt = tStop-tStart
        dT.append(dt)
    return dT
def swap(list,x,y):
    temp = list[x]
    list[x] = list[y]
    list[y] = temp
    return list
def selection_sort(list):
    for y in range(0,len(list)-1):
        xMin = y
        for x in range(y+1,len(list)):
            if list[x] < list[xMin]:
                xMin = x
        if xMin != y:
            swap(list,xMin,y)
    return list
def insertion_sort(list):
    for x in range(1,len(list)):
        valueToInsert = list[x]
        holePosition = x
        while holePosition > 0 and valueToInsert < list[holePosition-1]:
            list[holePosition] = list[holePosition-1]
            holePosition = holePosition - 1
        list[holePosition] = valueToInsert
    return list
def bubble_sort(list):
    swapped = True
    while swapped == True:
        swapped = False
        for x in range(1,len(list)):
            if list[x-1] > list[x]:
                swap(list,x-1,x)
                swapped = True
    return list
def quick_sort(list):
    if  len(list) <= 1:
        return list
    center = list.pop()
    less , great = [] , []
    for x in list:
        if x <= center:
            less.append(x)
        else:
            great.append(x)
    ans = quick_sort(less)
    ans.extend([center])
    ans.extend(quick_sort(great))
    return ans

def python_sort(list):
    list.sort()
    return list

mylist = random_list(20,0,100)
print mylist
print 'selection_sort' , selection_sort(mylist[:])
print 'insertion_sort' , insertion_sort(mylist[:])
print 'bubble_sort' , bubble_sort(mylist[:])
print 'quick_sort' , quick_sort(mylist[:])
print 'python_sort' , python_sort(mylist[:])

B = [10,1000,0.01,1]

subplot(221)
title('selection_sort')
axis(B)
A = myTest(selection_sort)
loglog(L,A)

subplot(222)
title('insertion_sort')
axis(B)
A = myTest(insertion_sort)
loglog(L,A)

subplot(223)
title('bubble_sort')
axis(B)
A = myTest(bubble_sort)
loglog(L,A)

subplot(224)
title('python_sort')
axis(B)
A = myTest(python_sort)
loglog(L,A)

show()


import time, itertools
from random import *
from matplotlib.pyplot import *

def random_list(N,a,b):
    return [randint(a,b) for i in range(N)]

X = range(10,1001,10)

def myTest(fun):
    dT = []
    for i in X:
        A = random_list(i,0,10)
        tStart = time.time()
        fun(A)
        tStop = time.time()
        dt = tStop-tStart
        dT.append(dt)
    return dT

def swap(list,i,j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    return list

def selection_sort(list):
    for j in range(0,len(list)-1):
        iMin = j
        for i in range(j+1,len(list)):
            if list[i] < list[iMin]:
                iMin = i
        if iMin != j:
            swap(list,iMin,j)
    return list

def insertion_sort(list):
    for i in range(1,len(list)):
        valueToInsert = list[i]
        holePos = i
        while holePos > 0 and valueToInsert < list[holePos-1]:
            list[holePos] = list[holePos-1]
            holePos = holePos - 1
        list[holePos] = valueToInsert
    return list



def bubble_sort(list):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(1,len(list)):
            if list[i-1] > list[i]:
                swap(list,i-1,i)
                swapped = True
    return list

def quick_sort(list):
    if  len(list) <= 1:
        return list
    pivot = list.pop()
    less , great = [] , []
    for x in list:
        if x <= pivot:
            less.append(x)
        else:
            great.append(x)
    ans = quick_sort(less)
    ans.extend([pivot])
    ans.extend(quick_sort(great))
    return ans
    
def python_sort(list):
    list.sort()
    return list

mylist = random_list(10,0,10)
print mylist
print 'selection sort' , selection_sort(mylist[:])
print 'insertion sort' , insertion_sort(mylist[:])
print 'bubble sort' , bubble_sort(mylist[:])
print 'quick sort' , quick_sort(mylist[:])
print 'python sort' , python_sort(mylist[:])

B = [10,1000,0.01,1]

subplot(221)
title('selection sort')
axis(B)
A = myTest(selection_sort)
loglog(X,A)

subplot(222)
title('insertion sort')
axis(B)
A = myTest(insertion_sort)
loglog(X,A)

subplot(223)
title('bubble sort')
axis(B)
A = myTest(bubble_sort)
loglog(X,A)

subplot(224)
title('python sort')
axis(B)
A = myTest(python_sort)
loglog(X,A)

show()

##B = [1,1000,0,0.25]
##
##subplot(221)
##title('selection sort')
##axis(B)
##A = myTest(selection_sort)
##plot(X,A)
##
##subplot(222)
##title('insertion sort')
##axis(B)
##A = myTest(insertion_sort)
##plot(X,A)
##
##subplot(223)
##title('bubble sort')
##axis(B)
##A = myTest(bubble_sort)
##plot(X,A)
##
##subplot(224)
##title('python sort')
##axis(B)
##A = myTest(python_sort)
##plot(X,A)
##
##show()


import random
import time
import matplotlib.pyplot as plt
import numpy as np


list = []
size1 = []
time1 = []
size2 = []
time2 = []
size3 = []
time3 = []
size4 = []
time4 = []

def random_list( N, a, b):
    #cleanlist
    del list[:]
    #create a list
    randnumber = [None] * N                     
    for i in range( 0, N):
        #Return a random integer x such that a <= x <= b
        randnumber[i] = random.randint( a, b)
    #extend takes a list as an argument and appends all of the elements
    list.extend(randnumber)


def insertion_sort(list):
    list_ = list
    for i in range( 1, len(list_)):
        j = i
        while j > 0 and list_[j - 1] > list_[j]:
            list_[j - 1], list_[j] = list_[j], list_[j - 1]
            j = j - 1

def selection_sort(list):
    list_ = list
    for i in range( 0, len(list_)):
        min = i
        for j in range( i+1,len(list_)): 
            if list_[j] < list_[min]:
                min = j
        list_[i], list_[min] = list_[min], list_[i]
            
    
def bubble_sort(list_):
    list_ = list
    for i in range( 0, len(list_)):
        for j in range( 1, len(list_)-i):
            if list_[j] < list_[j-1]:
                list_[j], list_[j-1] = list_[j-1], list_[j]

#time_insertion_sort
for i in range (1,11):
    random_list( i*1000, 0, 1000000)

    tStart = time.time()
    insertion_sort(list)  
    tEnd = time.time()
    size1.append(i*1000)   
    time1.append(tEnd - tStart)
    print 'Insertion',i*1000,tEnd - tStart

    tStart = time.time()
    selection_sort(list)
    tEnd = time.time()
    size2.append(i*1000)   
    time2.append(tEnd - tStart)
    print 'Selection',i*1000,tEnd - tStart

    tStart = time.time()
    bubble_sort(list)
    tEnd = time.time()
    size3.append(i*1000)   
    time3.append(tEnd - tStart)
    print 'Bubble',i*1000,tEnd - tStart

subplot(4, 1, 1)
plt.plot( size1, time1)
subplot(4, 1, 2)
plt.plot( size2, time2)
subplot(4, 1, 3)
plt.plot( size3, time3)
subplot(4, 1, 4)
plt.plot( size1, time1)
plt.plot( size2, time2)
plt.plot( size3, time3)
plt.show()

    











    

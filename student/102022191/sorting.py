import random
import time
import matplotlib.pylab

def random_list(N,a,b):
    res = []
    for i in range(N):
        res.append(random.randint(a,b))
    return res

def binary_search(s,l,r,value):
    while(l<r):
        mid = (l+r)/2
        if(s[mid]>value):
            r = mid
        else:
            l = mid +1
    return l

def selection_sort(s):
    for i in range(len(s)):
        index = i
        mini = s[i]
        for j in range(i,len(s)):
            if s[j]<mini:
                index, mini = j, s[j]
        s[i],s[index] = s[index], s[i]

def insertion_sort(s):
    for i in range(len(s)):
        insert = s[i]
        index = binary_search(s,0,i,insert)
        del s[i]
        s[index:index] = [insert]

def bubble_sort(s):
    for i in range(len(s)-1,0,-1):
        for j in range(0,i):
            if s[j]>s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]

def partition(s,l,r,index):
    value = s[index]
    s[index],s[r] = s[r], s[index]
    move = l
    for i in range(l,r):
        if s[i] < value:
            s[move],s[i] = s[i], s[move]
            move +=1
    s[r], s[move] = s[move], s[r]
    return move

def qsort(s,l,r):
    if l<r:
        new = partition(s,l,r,r)
        qsort(s,l,new-1)
        qsort(s,new+1,r)

def quick_sort(s):
    qsort(s,0,len(s)-1)


name = ['bubble_sort', 'selection_sort', 'insertion_sort', 'quick_sort']
function = [bubble_sort, selection_sort, insertion_sort, quick_sort]

x = range(1,5000,250)
y = [[],[],[],[]]
for num in x:
    s = random_list(num,1,10000000)
    for i in range(len(name)):
        new = s[:]
        start = time.time()
        function[i](new)
        end = time.time()
        y[i].append(end-start)
# plot
for i in range(len(name)):
    matplotlib.pylab.loglog(x,y[i])
matplotlib.pylab.xlabel('size')
matplotlib.pylab.ylabel('time')
matplotlib.pylab.legend(name)
matplotlib.pylab.show()



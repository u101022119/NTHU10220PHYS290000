Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
def random_list(N,a,b):
    c = []
    for i in range(N):
        c.append(random.randint(a,b))
    return c

def selection_sort(c,N):
    print random.sample(c,N)

def insertion_sort(c,N):
    for i in range(N):
        c.append(random.randint(a,b))
    print c
def bubble_sort(c):
    for i in range(len(c)):
        for j in range(len(c)-1):
            if c[j] < c[j+1]:
                temp = c[j]
                c[j] = c[j+1]
                c[j+1] = temp
    print c

a = 0
b = 100
insertion_sort(random_list(6,0,100),10)
bubble_sort(random_list(6,0,100))

import random
def random_list(N,a,b):
    x=[]
    for i in range(N):
        x.append(random.randint(a,b))
    return x

def selection_sort(x,N):
    print random.sample(x,N)

def insertion_sort(x,N):
    for i in range(N):
        x.append(random.randint(a,b))
    print x
def bubble_sort(x):
    for i in range(len(x)):
        for j in range(len(x)-1):
            if x[j] < x[j+1]:
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
    print x

a = 0
b = 100
insertion_sort(random_list(6,0,100),10)
bubble_sort(random_list(6,0,100))

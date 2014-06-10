import random
def random_list(N,a,b):
    p = []
    for i in range(N):
        p.append(random.randint(a,b))
    return p

def selection_sort(p,N):
    print random.sample(p,N)

def insertion_sort(p,N):
    for i in range(N):
        p.append(random.randint(a,b))
    print p
def bubble_sort(p):
    for i in range(len(p)):
        for j in range(len(p)-1):
            if p[j] < p[j+1]:
                temp = p[j]
                p[j] = p[j+1]
                p[j+1] = temp
    print p

a = 0
b = 100
insertion_sort(random_list(6,0,100),10)
bubble_sort(random_list(6,0,100))

    

import random

def random_list(N,a,b):
    li = []

    for i in range(N):
        li.append(random.randint(a,b))
        
    return li

	
def selection_sort(li,N):
    print random.sample(li,N)
    
	
def insertion_sort(c,N):
    
    for i in range(N):
        li.append(random.randint(a,b))
        
    print li



    
def bubble_sort(li):
    
    for i in range(len(li)):
	for j in range(len(li)-1):
            if li[j] < li[j+1]:
                temp = li[j]
	        lt[j] = li[j+1]
	        li[j+1] = temp
    print li


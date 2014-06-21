import random as r
def random_list(N,a,b):
    x=[]
    for i in range(N):
        x.append(r.randint(a,b))
    return x

def selection_sort(x):
    for i in range(len(x)):
        iMin=i
        for j in range(i+1,len(x)):
            if x[j]<x[iMin]:
                iMin=j
        
        x[i],x[iMin]=x[iMin],x[i]
    return x

def insertion_sort(x):
    for i in range(len(x)):
        tmp=x[i]
        for j in range(i,-1,-1):
            if tmp<x[j]:
                x[j]=x[j-1]
            if tmp>x[j]:
                x[j]=tmp
                break
    return x


x=random_list(5,7,15)

print x
print insertion_sort(x)


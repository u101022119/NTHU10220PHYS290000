import random

def random_list(N,a,b):
    l=[]
    for i in range(N):
        r=random.randint(a,b)
        l.append(r)

    print l

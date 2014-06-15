import math

def V(i,j,k):
    if i==0 and j==0 and k==0:
        return 0
    elif (i+j+k)%2==0:
        return (i**2+j**2+k**2)**-0.5
    elif (i+j+k)%2==1:
        return -((i**2+j**2+k**2)**-0.5)
    
L = int(raw_input('given L :'))
i = -L
j = -L
k = -L
summ = 0.0

while i<=L:
    while j<=L:
        while k<=L:
            summ = summ + V(i,j,k)
            k=k+1
        k=-L
        j=j+1
    j=-L
    i=i+1
print 'Madelung constant is',summ


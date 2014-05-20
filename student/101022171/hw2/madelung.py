import math

def V(i,j,k):
    if i==0 and j==0 and k==0:
        return 0
    elif (i+j+k)%2==0:
        return (i**2+j**2+k**2)**(-0.5)
    elif (i+j+k)%2==1:
        return -((i**2+j**2+k**2)**(-0.5))
    else:
        return "none"

L = int(raw_input("Enter L: ") )

summary = 0

i = -L
j = 0
k = 0
while i<=L:
    while j<=L:
        k=-L
        while k<=L:
            summary += V(i,j,k)
            k+=1
        j+=1
    j=-L
    i+=1

print summary

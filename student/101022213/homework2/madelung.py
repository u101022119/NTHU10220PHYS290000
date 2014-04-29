import math


def V(i,j,k):
    if i==0 and j==0 and k==0:
        return 0
    elif (i+j+k)%2==0:
        return (i**2+j**2+k**2)**-0.5
        #because chlorine atoms at positions
    elif (i+j+k)%2==1:
        return -((i**2+j**2+k**2)**-0.5)
        #because sodium atoms fall at positions
	    
L = int(raw_input('Input L :'))

i = j = k = -L  #all directions

total = 0.0

while i<=L:
    while j<=L:
        while k<=L:
            total = total + V(i,j,k)
            k=k+1
        k=-L
        j=j+1
    j=-L
    i=i+1
print total

import math

def M(i,j,k):
    if (i+j+k)%2==0:
        return 1/(math.sqrt(i**2+j**2+k**2))
    elif (i+j+k)%2==1:
        return -1/(math.sqrt(i**2+j**2+k**2))

def Madelung(L):
    tmp=0
    for i in range (-L,L+1):
        for j in range (-L,L+1):
            for k in range (-L,L+1):
                if i**2+j**2+k**2!=0: 
                    tmp+=M(i,j,k)
    print tmp

Madelung(100)

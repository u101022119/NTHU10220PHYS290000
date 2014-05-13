from math import *
myV={0:0}

def V(i,j,k):
    temp = i**2+j**2+k**2
    temp2 = i+j+k
    if temp not in myV:
        myV[temp]=1/sqrt(temp)
    ans = (-1)**temp2
    return ans*myV[temp]

def Vtot(L):
    ans = 0
    for i in range(-L,L+1):
        for j in range(-L,L+1):
            for k in range(-L,L+1):
                ans += V(i,j,k)
    return ans

print Vtot(200)



        


        

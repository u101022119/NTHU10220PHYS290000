import math
def potential(i, j, k):
    if i==0 and j==0 and k==0:
        return 0
    else:
        if (i+j+k)%2==0:
            return 1/math.sqrt(i**2+j**2+k**2)
        elif (i+j+k)%2==1:
            return -1/math.sqrt(i**2+j**2+k**2)

L=100
i=L
M=0
while i>=L*-1:
    j=L
    while j>=L*-1:
        k=L
        while k>=L*-1:
            M=M+potential(i, j, k)
            k-=1
        j-=1
    i-=1

print M

import math

L=300
i=-L
j=-L
k=-L
M=0
while i<=L:
    while j<=L:
        while k<=L:
            if i==j==k==0:
                M=M
            elif (i+j+k)%2==0:
                M=M+(i**2+j**2+k**2)**(-1.0/2.0)
            else :
                M=M-(i**2+j**2+k**2)**(-1.0/2.0)
            k=k+1
        j=j+1
        k=-L
    i=i+1
    j=-L
print M

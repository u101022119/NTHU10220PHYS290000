import math

def c(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if n>=1:
        return ((4.0*n-2.0)/(n+1.0))*c(n-1.0)
n=0
while c(n)<10**6:
    print c(n)
    n=n+1

import math
def c(n):
    if n == 0:
        return 1
    else:
        return (4*(n-1)+2)*c(n-1)/(n+1)
b = 0
while c(b)<1000000000:
    print c(b)
    b+=1
    

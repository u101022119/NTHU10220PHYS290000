import math

def catalan(n):
    if n == 0:
        return 1

    else:
        return catalan(n-1)*(4*n-2)/(n+1)
    n = n+1
        
for i in range(0,21):
    print i, catalan(i)


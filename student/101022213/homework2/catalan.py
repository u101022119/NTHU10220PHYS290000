
import math



def catalan(n):
        if n==0:
            return 1
        else:
            return catalan(n-1)*(4*n-2)/(n+1)
            
for i in range(19):
    print catalan(i)


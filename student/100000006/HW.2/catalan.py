
import math
def catalan(n):
    if n == 0:
        return 1
    else:
        return int((4*n-2.0)/(n+1.0)*catalan(n-1))


                
a = int(raw_input('input integer:'))
for i in range(a+1):
    print catalan(i),

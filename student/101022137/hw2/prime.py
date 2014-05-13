from math import *

myp=[2]

def Qprime(n):
    if n in myp:
        return True
    i = 0
    while myp[i] <= sqrt(n):
        if n%myp[i] == 0:
            return False
        i += 1
    myp.append(n)
    return True

for i in range(3,10000,2):
    print i , Qprime(i)
        
print myp

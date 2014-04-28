from __future__ import division
from math import *

def is_prime(n):
    a=2
    while (int(n/a)-n/a) !=0 and a<=n**(0.5) :
        a+=1
    if (int(n/a)-n/a) ==0:
        return False
    elif a>n**(0.5):
        return True

def prime_number(k):
    s=[2]
    for a in range(2,k+1,1):
        if is_prime(a)==True:
            s.append(a)
    print s

prime_number(10000)

    
        
    

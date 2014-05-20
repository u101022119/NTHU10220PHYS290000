from __future__ import division
from math import *

def is_prime(n):
    i=2
    while (int(n/i)-n/i) !=0 and i<=n**(0.5) :
        i+=1
    if (int(n/i)-n/i) ==0:
        return False
    elif i>n**(0.5):
        return True

def prime_number(k):
    s=[2]
    for i in range(2,k+1,1):
        if is_prime(i)==True:
            s.append(i)
    print s

prime_number(10000)

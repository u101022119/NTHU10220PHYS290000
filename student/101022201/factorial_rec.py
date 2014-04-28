import math

n=float(raw_input('n= '))

def factorial_rec(n):
    if int(math.fabs(n))!=n:
        print 'n has to be a nonnegative integer'
        return None
    elif n==0:
        return 1
    else:
        m=factorial_rec(n-1)
        p=n*m
        return p
print factorial_rec(n)

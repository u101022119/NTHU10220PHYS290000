import math
n=float(raw_input('n= '))
def factorial_rec(n):
    if int(math.fabs(n))!=n:
        print 'n must be an integer or be negative'
        return None
    elif n==0:
        return 1
    else:
        m=factorial_rec(n-1)
        A=n*m
        return A
print factorial_rec(n)


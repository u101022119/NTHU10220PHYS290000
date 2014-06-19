from pylab import *

def LogisticMap(r,n,k):
    if n==0:
        return k
    else:
        c=LogisticMap(r,n-1,k)
        return r*c*(1-c)
#if you write return r*LogisticMap(r,n-1,k)*(1-LogisticMap(r,n-1,k)) here
#it won't work !
r = arange(1,4,0.01)
x = LogisticMap(r,500,0.5)
xlabel('r')
ylabel('x')
title('logistic map')
plot(r,x)

show()

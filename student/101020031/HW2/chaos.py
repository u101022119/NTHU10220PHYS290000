from math import *
from pylab import *

def map(n,r):
    if n==0:
        return 0.5
    else:
        k=map(n-1,r)
        return r*k*(1-k)
r=arange(1,4,0.01)
x=map(100,r)
xlabel("y")
ylabel("x")
title("logistic map")
plot(r,x)

show()

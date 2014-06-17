from math import *
from pylab import *


def Logistic_Map(n,r):
    if n==0:
        return 0.5
    else:
        k = Logistic_Map(n-1,r)
        return r*k*(1-k)
    
r = arange(1, 4, 0.01)
x = Logistic_Map(100,r)
xlabel('r')
ylabel('x')
title('logistic map')
plot(r,x)

show()

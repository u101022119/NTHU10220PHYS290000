from math import *
from pylab import *
sys.setrecursionlimit(1500)

def LogMap(n,r):
    if n == 0:
        return 0.5
    a = LogMap(n-1,r)
    ans = r*a*(1.-a)
    return ans

r = arange(1,4,0.01)
x = [LogMap(1000,i) for i in r]
plot(r,x)
show()


    

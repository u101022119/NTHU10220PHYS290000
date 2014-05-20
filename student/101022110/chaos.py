from matplotlib.pylab import *

def chaos(r, x):
    return r*x*(1-x) 

def rec(r, x):
    t=1000
    while t>0:
        x=chaos(r, x)
        t-=1
    return x

rlist=[r*0.01 for r in range(100, 400)]
xlist=zeros(len(rlist))

for i in xrange(len(rlist)):
    x=0.5
    xlist[i]=rec(rlist[i], x)

plot(rlist, xlist)
axis([1, 4, 0, 1])
show()
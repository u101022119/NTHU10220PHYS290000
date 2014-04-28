from matplotlib.pylab import *
import matplotlib.pyplot as plt
import numpy as np

def logistic(x,r):
    p=[]
    q=[]
    for i in range(1000):
        s=r*x*(1-x)
        if s==x:
            return s
        elif s!=x and s in p:
            if s not in q:
                q.append(s)
        else:
            p.append(s)
        x=s
    z=np.zeros(len(q))
    for i in xrange(len(q)):
        z[i]=q[i]
    return z

        
for r in linspace(1,4,301):
    x1=logistic(0.5,r)
    p=np.zeros(x1.size)
    for i in xrange(x1.size):
        p[i]=r
    plt.plot(p,x1,'bo')

xlabel('r')
ylabel('x')
axis([1.0, 4.0, 0.0, 1.0])

show()
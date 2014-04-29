import numpy as np
from matplotlib.pylab import *

def thousand_time(r):
    x=0.5
    for i in range(1000):
        x=r*x*(1-x)
    return x

r = np.arange(1,4.01,0.01)
x = thousand_time(r)

plot(r,x)
show()

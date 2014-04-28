from numpy import *
from matplotlib.pylab import *

def logistic_map(x,r):
    return r*x*(1-x)

def iterate_logistic(r):
    now = 0.6248315
    N = int(r**2*1500)
    if r>3.5:
        N = 70000
    for i in range(N):#iterate N times
        now = logistic_map(now,r)
    '''look = dict()#find cycle
    while not look.has_key(now):
        look[now] = 0
        now = logistic_map(now,r)'''
    res = dict()#find values
    while not res.has_key(now):
        if len(res) < 500:
            res[now] = 0
            now = logistic_map(now,r)
        else:
            break
    return res.keys()

def do_chaos(r_min,r_max):
    r_value = []
    x_value = []
    rrange = linspace(r_min,r_max,int((r_max-r_min)/0.01)+1)
    for r in rrange:
        look = iterate_logistic(r)
        for cnt in range(len(look)):
            r_value.append(r)
            x_value.append(look[cnt])
    return array(r_value) , array(x_value)

if __name__ == '__main__':
    r, x =do_chaos(1.0,3.9)
    scatter(r,x)
    show()

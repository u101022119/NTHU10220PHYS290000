def f(x):
    return x**4
n=7
dx= 1.0/(n-1)
xlist= [i*dx for i in range(n)]
ylist= [f(x) for x in xlist]
pairs= [[x,y] for x,y in zip(xlist,ylist)]

print pairs

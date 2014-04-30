from pylab import *
x=0.5
r=arange(1,4,0.01)


for k in range(1000):
    x=r*x*(1-x)
    xlabel('r')
    ylabel('x')
    title('logistic map ³æ®p¬M¹³')

    plot(r,x)
    show()

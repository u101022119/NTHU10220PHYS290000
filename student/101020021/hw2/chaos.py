
from pylab import *
r=arange(1,4,0.01)


for i in xrange(len(r)) :
    ans=[]
    repeat=[]
    x=0.5
    s=0
    j=0
    for j in range(1000):
        s=r[i]*x*(1-x)
        repeat.append(round(x,4))
        if round(s,4) in repeat :
            ans.append(s)
        x=s
    abc=np.zeros(len(ans))
    for k in xrange(len(abc)):
        abc[k]=r[i]
    plot(abc,ans,'k.')
show()

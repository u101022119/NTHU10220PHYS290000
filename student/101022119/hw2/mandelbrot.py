from math import *
from pylab import *


x=arange(-2,2,0.02)
y=arange(-2,2,0.02)

real=[]
im=[]
x1=empty([len(x),len(y)],float)
for i in range(len(x)):
    for j in range(len(y)):
        c=complex(x[i],y[i])
        z=0+0j
        for k in range(100):
            z=z**2+c
            if abs(z)>2:
                x1[j,i]=k
                break

            if abs(z)<=2:
                x1[j,i]=abs(z)*100
                real.append(x[i])
                im.append(y[j])
plot(real,im,"k")
imshow(x1,origin="O",extent=[-2,2,-2,2])
hot()
show()

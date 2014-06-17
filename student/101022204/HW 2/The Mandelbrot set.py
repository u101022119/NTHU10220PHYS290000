from pylab import *

x = arange(-2,2,0.01)
y = arange(-2,2,0.01)
real = []
image = []
X = empty([len(x),len(y)],float)
for i in range(len(x)):
    for j in range(len(y)):
        c = complex(x[i],y[j])
        z = 0+0j
        for k in range(100):
            z=z**2+c
            if abs(z)>2:
                X[j,i] = k
                break
            
        if abs(z)<=2:
            X[j,i] = abs(z)*100
            real.append(x[i])
            image.append(y[j])
            
imshow(X,origin="lower",extent=[-2,2,-2,2])
jet()
show()

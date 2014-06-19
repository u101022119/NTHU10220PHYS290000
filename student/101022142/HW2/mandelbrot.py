from pylab import *
#N is what you need to give !
N=int(raw_input("give a interger N. "))

x=linspace(-2,2,N)
y=linspace(-2,2,N)

X=[]
Y=[]
S=empty([len(x),len(y)],float)

for m in range(len(x)):
    for n in range(len(y)):
        c=x[m]+y[n]*1j    #1j !=j
        z=0+0j
        for k in range(N):
            z=z**2+c
            if abs(z)>2:
                S[n,m]=k
                break
            if abs(z)<=2:
                S[n,m]=abs(z)*N
                X.append(x[m])
                Y.append(y[n])
                
plot(X,Y,"k")
imshow(S,origin="O",extent=[-2,2,-2,2])
jet()
show()

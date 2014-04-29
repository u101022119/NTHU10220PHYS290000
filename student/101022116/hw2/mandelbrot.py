from cmath import *
from pylab import *
sys.setrecursionlimit(1500)

def myz(c,n):
    z = {0:0.}
    for i in range(1,n+1):
         z[i] = z[i-1]**2 + c
         if abs(z[i]) > 2.0:
             return 2.
    return abs(z[i])

def Mandelbrot (x,y,n):
    c = complex(x,y)
    return myz(c,n)
 
x = arange(-2,2,0.005)
y = arange(-2,2,0.005)
data =[[Mandelbrot(i,j,100) for i in x] for j in y] 
imshow(data)
xlabel("real")
ylabel("image")
show()

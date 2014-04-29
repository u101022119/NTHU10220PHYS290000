from matplotlib.pylab import *

MAX_ITERATE = 200
N = 300
side = 2.0
spacing = side / N


def Mandelbrot(c):
    cnt = 0
    z=0
    while cnt<MAX_ITERATE and (z*z.conjugate()).real<4.0:
        z = z**2 +c
        cnt += 1 
    return cnt

xi = empty([N*2,N*2],int)
for i in range(-N,N):
    y = spacing * i
    for j in range(-N,N):
        x = spacing *j
        xi[i,j] = Mandelbrot(complex(x,y))

imshow(xi,origin='lower',extent=[-side,side,-side,side])
hot()
show()

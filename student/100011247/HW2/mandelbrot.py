import math
import numpy as np
from matplotlib.pylab import *
Nx=[]
Ny=[]

def iterate(x,y):
	a=0
	b=0	
	for i in range(100):
		A=a**2-b**2+x
		B=2*a*b+y
		a=round(A,5)
		b=round(B,5)
		z=a**2+b**2
		if z>2:
			Nx.append(x)	
			Ny.append(y)
			break	
	return i

for i in np.arange(-2,3,0.05):
	for j in np.arange(-2,3,0.05):
		iterate(i,j)

plt.scatter(Nx,Ny)
plt.show()

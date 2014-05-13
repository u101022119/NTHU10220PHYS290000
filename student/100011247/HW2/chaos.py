import matplotlib.pyplot as plt
from numpy import arange
x=0.5
List=[]
r=[]

def logistic_map(i):
	global x
	for j in range(999):
		x=i*x*(1-x)
	return x

for i in arange(1,5,0.001):
	logistic_map(i)
	r.append(i)
	List.append(x)			
	
plt.scatter(r,List)
plt.xlabel("r")
plt.ylabel("x")
plt.xlim(1,4)
plt.title("The Deterministic Chaos Demo")
plt.show()

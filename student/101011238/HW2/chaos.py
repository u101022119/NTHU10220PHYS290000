import numpy as np
import matplotlib.pyplot as plt

def f(x, r):
    return r*x*(1-x)
    
ys = []
rs = np.linspace(1, 4, 300)

for r in rs:
    x = 0.5
    for i in range(500):
        x = f(x, r)

    for i in range(50):
        x = f(x, r)
        ys.append([r, x])

ys = np.array(ys)

plt.plot(ys[:,0], ys[:,1], '.')
plt.xlabel('r')
plt.ylabel('x')
plt.show()
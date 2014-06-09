import matplotlib.pyplot as plt
import numpy as np

n = 200
x = np.linspace(-2,2,n)
y = np.linspace(-2,2,n)

a1 = np.zeros(n**2)
a2 = np.zeros(n**2)

for i in range(n):
    for j in range(n):
        z = 0 + 0j
        for k in range(100):
            z = z**2+(x[i]+y[j]*1j)
            if z*z.conjugate()>4:
                break            
        if z*z.conjugate()<4:
            a1[n*i+j] = x[i]
            a2[n*i+j] = y[j]

plt.plot(a1,a2,'k.')
plt.show()

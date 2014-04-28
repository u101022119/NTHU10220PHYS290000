import numpy as np
A=[1 ,2 ,3 ,4 ,5 ,6]
print A
a=np.array(A)
from numpy import array,linspace
b=array(A)
print a
print b
print a[1:-1]
print 'a4=',a[4]
c=a[1:-1]
print 'a?=',a[4]

c[3]=22
print 'c3=',c[3]
print 'a4=',a[4]
print'c1=',c[0]

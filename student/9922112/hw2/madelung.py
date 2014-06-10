# -*- coding: utf-8 -*-
"""
Created on Mon May 12 21:10:33 2014

@author: Administrator
"""


L=20
D=range(-L,L+1)
P=[]
for i in D: 
    for j in D:
        for k in D:
            P.append([i,j,k])
P.remove([0,0,0])
M=[]
for l in P:
    d=1/math.sqrt(l[0]**2+l[1]**2+l[2]**2)
    if sum(l)%2==0:
        M.append(d)            
    else:
        M.append(-d)
print 'the Madelung constant is aprroximate equal',sum(M)


            


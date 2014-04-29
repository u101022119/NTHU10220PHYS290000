import math

L=50
i=-L
j=-L
k=-L
m=0

for x in range(-L,L+1):
    for y in range(-L,L+1):
        for z in range(-L,L+1):
            if x==0 and y==0 and z==0:
                pass
            elif (x+y+z)-(x+y+z)/2==(x+y+z)/2:
                v=float(1/(math.sqrt(x*x+y*y+z*z)))
                m+=v
            else:
                v=float(-1/(math.sqrt(x*x+y*y+z*z)))
                m+=v

print m

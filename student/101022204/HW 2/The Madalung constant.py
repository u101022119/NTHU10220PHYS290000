import math
def madelung(l):
    x=0
    for i in range(1,l+1):
        for j in range (1,l+1):
            for k in range(1,l+1):
                x = (-1)**(i+j+k+1)/math.sqrt(i**2+j**2+k**2)
    y=0
    i=0
    for j in range (1,l+1):
            for k in range(1,l+1):
                y = (-1)**(j+k+1)/math.sqrt(j**2+k**2)
    z=0
    i=0
    j=0
    for k in range(1,l+1):
                x = (-1)**(k+1)/math.sqrt(k**2)
    a = x*8+y*12+z*6
    print a

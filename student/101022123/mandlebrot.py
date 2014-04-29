import math
def madelung(l):
    a=0
    for i in range(1,l+1):
        for j in range (1,l+1):
            for k in range(1,l+1):
                a = (-1)**(i+j+k+1)/math.sqrt(i**2+j**2+k**2)
                b=0
                i=0
                for j in range (1,l+1):
                    for k in range(1,l+1):
                        b = (-1)**(j+k+1)/math.sqrt(j**2+k**2)
                        c=0
                        i=0
                        j=0
                        for k in range(1,l+1):
                            a = (-1)**(k+1)/math.sqrt(k**2)
                            m = a*8+b*12+c*6
                            print m

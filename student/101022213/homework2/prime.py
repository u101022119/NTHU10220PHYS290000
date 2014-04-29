import math


def prime(x):
    m = math.floor(x**0.5)
    y=2
    z=0
    while y <= m :
        if x%y==0:
            y=y+1
            z=z+1
        else:
            y=y+1
    if z == 0:
        print x,"is prime"
    else:
        print x, "is not prime"

print"this prime judge is start form N to M"      
N= int(raw_input('Input N :'))
M= int(raw_input('Input N :'))


      
a = range(M+1)
for i in a[N:]:
    prime(i)      

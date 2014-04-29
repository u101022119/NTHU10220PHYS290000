def madelung_constant(L):
    a=0
    for i in range(-L,L+1,1):
        for j in range(-L,L+1,1):
            for k in range(-L,L+1,1):
                if (i,j,k)==(0,0,0):
                    k+=1
                else:
                    b=(-1)**(i+j+k)/(i**2+j**2+k**2)**(0.5)
                    a+=b
    return a

print 'madelung_constant=-1.748'
print madelung_constant(150)
                    

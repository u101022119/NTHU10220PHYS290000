def m(l):
    t=0
    for i in range(-l,l+1,1):
        for j in range(-l,l+1,1):
            for k in range(-l,l+1,1):
                if (i,j,k)==(0,0,0):
                    k+=1
                else:
                    s=(-1)**(i+j+k)/(i**2+j**2+k**2)**(0.5)
                    t+=s
    return t
    
# m(500)==-1.746411
# m(200)==-1.744685
# Madelung Constant==-1.748

M=int(raw_input('What is your L : '))
import math
def madelung(L):
    i=-L
    j=-L
    k=-L
    p=0
    while i<L+1:
        while j<L+1:
            while k<L+1:
                if k==0:
                    k=k+1                    
                else:
                    n=(-1)**(i+j+k)*1/math.sqrt(i*i+j*j+k*k)
                    p=n+p
                    k=k+1                    
            j=j+1
            k=-L
            if j==0:
                j=j+1                
            else:
                while k<L:
                    if k==0:
                        k=k+1                        
                    else:
                        n=(-1)**(i+j+k)*1/math.sqrt(i*i+j*j+k*k)
                        p=n+p
                        k=k+1                     
        i=i+1
        j=-L
        if i==0:
            i=i+1            
        else:
            while j<L:
                while k<L:
                    if k==0:
                        k=k+1                        
                    else:
                        n=(-1)**(i+j+k)*1/math.sqrt(i*i+j*j+k*k)
                        p=n+p
                        k=k+1                        
                j=j+1
                k=-L
                if j==0:
                    j=j+1                    
                else:
                    while k<L:
                        if k==0:
                            k=k+1                            
                        else:
                            n=(-1)**(i+j+k)*1/math.sqrt(i*i+j*j+k*k)
                            p=n+p
                            k=k+1                           
    print p
madelung(M)

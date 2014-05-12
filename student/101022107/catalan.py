def Catlalan(n):
    if n==0:
        
        return 1
    else:
        
        return (4*n+2)*Catlalan(n-1)/(n+2)
        
n=0
while Catlalan(n)<=1000000:
    print Catlalan(n)
    n=n+1
            
                        
              
             
            


        

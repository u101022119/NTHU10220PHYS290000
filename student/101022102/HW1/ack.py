def A(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        g = A(m-1,1)
        return g
    elif m>0 and n>0:
        k = A(m,n-1)
        j = A(m-1,k)
        return j
    
        
    


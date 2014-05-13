def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    else:
        return ack(m-1,ack(m,n-1))
    
#python errored when m become lager. 
#Ack(m,n) grow very fast whit incresing m.
#Python returned that the maximum depth of loop where exceeded.
    
        

def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        m=m-1
        return ack(m,1)
    elif m>0 and n>0:
        n = ack(m,n-1)
        m=m-1
        return ack(m,n)
    

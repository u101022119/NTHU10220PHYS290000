def ack(m,n):
    if m==0:
        Ans=n+1
        print Ans
    elif m>0 and n==0:
        m=m-1
        n=1
        return m,n
    elif m>0 and n>0:
        m=m-1
        n=ack(m,n-1)
        return m,n
ack(3,4)

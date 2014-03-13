def ack(m,n):
    if m==0:
        s=n+1
        return s
    elif m>0 and n==0:
        s=ack(m-1,1)
        return s
    elif m>0 and n>0:
        s=ack(m-1,ack(m,n-1))
        return s
    else:
        return 'None'

print "A(3,4) is ", ack(3,4)

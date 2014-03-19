while True:
    def ack(m,n):
        if m==0:
            return n+1
        elif m>0 and n==0:
            return ack(m-1,1)
        elif m>0 and n>0:
            return ack(m-1,ack(m,n-1))

    print 'Input the compoment:'
    m = float(raw_input())
    n = float(raw_input())

    print ack(m,n)

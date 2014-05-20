#10.Ackermann function
def ack(m,n):
    if type(m) and type(n)==int:
        if m==0:
            return n+1
        if m>0:
            if n==0:
                return ack(m-1,1)
            if n>0:
                return ack(m-1,ack(m,n-1))
        else :
            print "m,n should be positve number or 0"
    else :
        print "m,n should be positve number or 0"
print ack(3,4)
#you can discover that if m>=4,the vaule will be terrible!
#when m decreasing,n 's increasing has no limiting......

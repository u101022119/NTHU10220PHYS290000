def ack(m,n):
    if n<0 or m<0 or n-int(n)!=0 or m-int(m)!=0:
        return 'Ackermann function is not for negative number'
    else:
        if m==0:
            return n+1
        elif m>0 and n==0:
            return ack(m-1, 1)
        elif m>0 and n>0:
            return ack(m-1, ack(m, n-1))

print 'a(3, 4)\n', ack(3, 4)
print 'a(-3, 1)\n', ack(-3, 1)
print 'a(5, 2.2)\n', ack(5, 2.2)

def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))

print "ack(3,4) = " , ack(3,4)

print "Please input m and n"
m=int(raw_input())
n=int(raw_input())
print "ack(",m,",",n,") = ",ack(m,n)

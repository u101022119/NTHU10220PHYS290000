p = []
try:
    p.append( float(raw_input('Put m here.')) )
    p.append( float(raw_input('Put n here.')) )
except ValueError:
    print "Error!"


def Ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return Ack(m-1,1)
    elif m>0 and n>0:
        return Ack(m-1,Ack(m,n-1))

print Ack(p[0],p[1])    

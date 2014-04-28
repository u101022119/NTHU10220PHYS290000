def ack(m,n):
    if not isinstance(n,int):
        print 'Factorial is only defined for integers.'
        return None
    elif n < 0:
        print 'Factorial is not defined for negative integers.'
        return None    
    elif m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))

print 'ack(x,y)'
x=input('x=')
y=input('y=')

print ack(x,y)

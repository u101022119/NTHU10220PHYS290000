Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
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

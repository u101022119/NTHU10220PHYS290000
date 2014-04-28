def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))
    else:
        return 'None'

print ack(3,4)

'''
for m>=4, this function doesn't work
because of the result of ack-function is too large. 




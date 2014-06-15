


def ack(m,n):
    if m == 0:
        ans = n+1
    elif m > 0 and n == 0:
        ans = ack(m-1,1)
    elif m > 0 and n > 0:
        ans = ack(m-1,ack(m,n-1))
    else:
        print "ERROR!!"
        return
    return ans

print "ack(3,4) = ",ack(3,4)

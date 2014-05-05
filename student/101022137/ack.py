m, n=float(raw_input( 'ENTER THE VALUE OF m:')), float(raw_input( 'ENTER THE VALUE OF n:'))
def ach(m, n):
    if n<0:
        return none
    elif m<0:
        return none
    elif m==0:
        return n+1
    elif n==0:
        return ach(m-1,n)
    else:
        return ach(m-1,ach(m,n-1))
print ach(m, n)

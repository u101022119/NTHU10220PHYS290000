n=(float(raw_input("Put n here.")))
def fac(n):
    if n==0:
       return 1
    elif n>0:    
        return n*fac(n-1)
    else:
        return 0
if fac(n)>0:
    print fac(n)
elif n<0 or type(n)!=int or type(n)!=str:
    print 'Error, the n given should not be negative and should be integer.'

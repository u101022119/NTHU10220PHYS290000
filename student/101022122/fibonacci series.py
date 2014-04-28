
n=input('enter the fibonacci number:')
def fi(n):
    if n<0:
        pass
    elif not isinstance(n,int):
        pass
    else:
        if n==1:
            return 1
        elif n==2:
            return 1
        else:
            return fi(n-1)+fi(n-2)

def print_fi(n):
    f1=1
    f2=1
    if n<0:
        print 'fibonacci number cannot be negative'
    elif not isinstance(n,int):
        print 'fibonacci number need to be integer'
    elif n==1:
        print '1'
    else:
        while f1<=fi(n):
            print f1,''
            f1,f2=f2,f1+f2

fi(n)
print_fi(n)

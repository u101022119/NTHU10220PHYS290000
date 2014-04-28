n=float(raw_input("Put n here."))
def fibonacci_rec(n):
    if n==1:
        return 1
    if n>1:
        return n+fibonacci_rec(n-1)
    else:
        return 0
if fibonacci_rec(n)>0:
    print fibonacci_rec(n)
elif n<0 or type(n)!=int or type(n)!=str:
    print 'Error, the n given should positive and should be an integer.'


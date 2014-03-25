def fibonacci_rec(n):
    if not isinstance(n,int):
        print 'None'
    elif n<0:
        print 'None'
    elif n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return fibonacci_rec(n-1)+fibonacci_rec(n-2)
        
def do_fibonacci_rec(n):
    x=n
    n=0
    while n<=x:
        print fibonacci_rec(n)
        n=n+1
        

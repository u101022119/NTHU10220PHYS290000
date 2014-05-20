def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print 'please enter fibonacci_rec(0,n)'

def fibonacci_rec(m,n):
    if n<0 or n%1 != 0:
        print "error"
    elif m >= n:
        return 0
    else:
        print fibonacci (m)
        fibonacci_rec(m+1,n)
    





    


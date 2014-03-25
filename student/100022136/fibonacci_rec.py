def fibonacci(n):
    if n==1:
        return 1
    if n==0:
        return 0
    value = fibonacci(n-1)+fibonacci(n-2)
    return value
def fibonacci_rec(n):
    if n%1!=0 or n<=0:
        print 'Stop kidding me!\nPlease enter a natural number'
        return None
    for i in range(n):
        print 'f({0})={1}'.format(i+1,fibonacci(i+1))
    return fibonacci(n)
fibonacci_rec(10)
fibonacci_rec(1.414)
        

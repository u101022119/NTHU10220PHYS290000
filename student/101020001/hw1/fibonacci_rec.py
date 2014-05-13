
def fibonacci_rec(n):
    if not isinstance(n, int):
        print 'Factorial is only defined for integers.'
    elif n==0:
        return 0
    elif n<0:
        print 'Factorial is not defined for negative integers.'
    elif n==1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

    

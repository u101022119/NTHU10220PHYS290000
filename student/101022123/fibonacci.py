def fibonacci (n):
    if not isinstance(n, int):
        print 'Factorial is only defined for integers.'
        return None
    elif n < 0:
        print 'Factorial is not defined for negative integers.'
        return None
    elif n == 0:
        
        return 0    
    elif n == 1:
        
        return 1   
    else:
        print n
        return fibonacci(n-1) + fibonacci(n-2)
    
fibonacci(n)


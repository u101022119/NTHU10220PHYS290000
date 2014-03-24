def factorial(n):
    if not isinstance(n, int):
        print 'invalid input'
        return None
    elif n==0:
        return 1
    elif n<0:
        print 'invalid input'
        return None
    else:
        rec= factorial(n-1)
        result= n*rec
        return result
    

def factorial_rec(n):
    if not isinstance(n,int):
        print'Factorial is only defined for integers.'
        print None
    elif n<0:
        print'Factorial is not defined for negative integers.'
        print None
    elif n==0:
        return 1
    else:
        return n*factorial_rec(n-1)

    

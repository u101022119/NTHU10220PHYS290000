def factorial_rec (n):
    if not isinstance(n, int):
        print 'X! Factorial is only defined for integers.'
        return None
    elif n < 0:
        print 'X! Factorial is not defined for negative integers.'
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial_rec(n-1)

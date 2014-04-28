def factorial_rec(n):
    if not isinstance(n, int):
        print 'Factorial is only defined for integers.'
        return None
    elif n < 0:
        print 'Factorial is not defined for negative integers.'
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial_rec(n-1)

print 'Ha-Ha!I am FACTORIAL CLACULATER!'
x = input('Give me a number!')

factorial_rec(x)










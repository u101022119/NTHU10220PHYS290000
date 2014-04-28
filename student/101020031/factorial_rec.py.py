def factorial_rec(n):
    if not isinstance(n,int):
        print "factorial is only defined for integers."
        return None
    elif n<0:
        print "factorial is not defined for negative integers."
        return None
    elif n==0:
        return 1
    else:
        return n * factorial_rec(n-1)


print factorial_rec(5)

    

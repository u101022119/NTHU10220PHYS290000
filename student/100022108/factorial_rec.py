def factorial_rec(n):
    if n<0:
        print "error"
    elif n%1 != 0:
        print "error"
    elif n == 0:
        return 1
    else:
        recurse = factorial_rec(n-1)
        result = n * recurse
        return result

def factorial(n):
    if n==0:
        return 1
    elif not isinstance(n,int):
        print"factorial is defined for integer "
    elif n>0:
        recurse = factorial(n-1)
        return n*recurse
    elif n<0:
        print "factorial is not for negative interger"
    

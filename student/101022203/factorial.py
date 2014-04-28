def fibonacci(n):
    if not isinstance(n,int):
        print'fibonacci is not defined for non-integer'
        print'none'

    elif n<0:
        print'fibonacci is not defined for negative numbers'
        print'none'

    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return finonacci(n-1)+fibonacci(n-2)

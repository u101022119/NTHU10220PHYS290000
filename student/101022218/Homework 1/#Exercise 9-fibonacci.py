def fibonacci_rec(n):
    if type(n)!=int:
        return"None"
    elif n<=0:
        return"None"
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
        a=fibonacci_rec(n-2)+fibonacci_rec(n-1)
        return a

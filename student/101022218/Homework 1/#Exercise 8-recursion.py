def factorial_rec(n):
    if type(n)!=int :
        return "None"
    elif n<0:
        return "None"
    elif n==0:
        return 1
    else:
        b=factorial_rec(n-1)
        a=n*b
        return a

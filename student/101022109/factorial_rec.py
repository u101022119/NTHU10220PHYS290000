def factorial_rec(n):
    if n<0:
        return 'NOOOOO!factorial function is not defined for negative numbers!!'
    elif n-int(n)!=0:
        return 'OH!factorial function is defined for integers!!'
    else:
        if n==0:
            return 1
        else:
            result=n*factorial_rec(n-1)
            return result
print factorial_rec(5)
print factorial_rec(-8)
print factorial_rec(2.4)

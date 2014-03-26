def fibonacci_rec(n):
    if not isinstance(n,int):
        print 'Factorial is only defined for integers.'
        return None
    elif n < 0:
        print 'Factorial is not defined for negative integers.'
        return None
    elif n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        result=fibonacci_rec (n-1)+fibonacci_rec (n-2)
        return result
    
n=input('n=:')
print fibonacci_rec (n)

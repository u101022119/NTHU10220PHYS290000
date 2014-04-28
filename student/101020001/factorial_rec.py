def recurse():
    recurse()
def factorial_rec(n):

    if not isinstance(n, int):
        print 'Factorial is only defined for integers.'
    elif n==0:
        return 1
    elif n<0:
        print 'Factorial is not defined for negative integers.'
    else:
        recurse=factorial_rec(n-1)
        k=recurse*n
        return k
        

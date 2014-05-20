import math
n=float(raw_input(' ENTER THE VALUE OF n: '))
def factorial_rec(n):
    if n<0:
        return none
    elif n!=int(n):
        return none
    else:
        if n==0:
            return 1
        else:
            recurse=factorial_rec(n-1)
            result=n*recurse
            return result
print 'The factorial n is', factorial_rec(n)        
    

n=float(raw_input(' ENTER THE VALUE OF n: '))
def fibonacci_rec(n):
    if n<0:
        return none
    elif n!=int(n):
        return none
    else:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return fibonacci_rec(n-1)+fibonacci_rec(n-2)
print 'The fibonacci n is', fibonacci_rec(n)      

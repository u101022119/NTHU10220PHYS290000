def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
def factorial_rec(n):
    if n%1==0 and n>0:
        value = factorial(n)
        print value
        return value
    print 'Are you kidding me?\nPlease enter a natural number'
    return None
factorial_rec(6)
factorial_rec(-1)

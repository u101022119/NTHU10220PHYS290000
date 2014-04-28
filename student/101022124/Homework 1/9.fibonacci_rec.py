
def fibonacci_rec(n):
    if n == 0:
        return 0
    elif type(n) is not int:
        print "None"
        return None
    elif n<0:
        print "None"
        return None
    elif n==1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)
        



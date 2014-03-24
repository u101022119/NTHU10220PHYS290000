
def factorial_rec(n):
    if type(n) is not int:
        print "None"
        return None
    elif n < 0:
        print "None"
        return None
    elif n == 0:
        return 1
    else:
        a = n*factorial_rec(n-1)
        return a


n = float( raw_input("Enter number:") )        
factorial_rec(n)

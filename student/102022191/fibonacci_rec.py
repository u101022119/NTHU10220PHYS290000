
def fibonacci(n):
    if n==1 or n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def is_int(s):
    for x in s:
        if x>'9' or x<'0':
            return False
    return True

def fibonacci_rec(s):
    if is_int(s)==False:
        print "ERROR"
        return None
    n=int(s)
    for x in range(1,n+1):
        print "f(",x,")=",fibonacci(x)

print "Demostration fibonacci_rec(12)"
fibonacci_rec("12")

print "Demostration fibonacci_rec(1.2)"
fibonacci_rec("1.2")

inp = raw_input("Please input the n\n")
fibonacci_rec(inp)

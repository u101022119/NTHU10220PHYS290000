
def is_int(s):
    for x in s:
        if x>'9' or x<'0':
            return False
    return True

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

def factorial_rec(s):
    if is_int(s)==False:
        print ("Error")
        return None
    n=int(s)
    print factorial(n)

print "Demostration factorial_rec(10)"
factorial_rec("10")

print "Demostration factorial_rec(1.2)"
factorial_rec("1.2")

inp=raw_input("Please input the n\n")
factorial_rec(inp)

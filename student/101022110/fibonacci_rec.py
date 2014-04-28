def recpart(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return recpart(n-1)+recpart(n-2)

def fibonacci(n):
    if n<=0:
        return 'factorial function is for positive numbers'
    elif n-int(n)!=0:
        return 'factorial function is for integers'
    else:
        for i in range(n-1):
            print recpart(i+1)
        return recpart(n)

print "f(6)\n", fibonacci(6)
print "f(-2)\n", fibonacci(-2)
print "f(3.3)\n", fibonacci(3.3)

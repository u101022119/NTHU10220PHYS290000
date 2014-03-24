def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>0 and n==int(n):
        return fibonacci(n-1)+fibonacci(n-2)
    else:
        return None

n=input("n of fibonacci(n):")
print " fibonacci(",n,") is",fibonacci(n)

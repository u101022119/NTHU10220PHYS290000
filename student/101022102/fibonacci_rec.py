def fibonacci(n):
    if not isinstance(n,int):
        print"fibonacci is defined for integer"
    elif n<0:
        print"fibonacci is not for negative"
    elif n==0:
        return 0
    elif n==1:
        return 1
    elif n>=2 :
        return fibonacci(n-1) + fibonacci(n-2)
    
    

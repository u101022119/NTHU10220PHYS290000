def factorial(n):
    if not isinstance(n, int):
        print'Hey guy! this function is only defined for integers>0!'
    elif n<0:
        print'Hey guy! this function is only defined for integers>0'
    elif n==0:
        return 1
    else:
        result=n*factorial(n-1)
        return result
        

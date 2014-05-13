#8.fibonacci_rec.py
def fibonacci_rec(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if n>1 and (type(n)==int or long):
        return fibonacci_rec(n-1)+fibonacci_rec(n-2)
    else:
        print 'Wrong!n should be positive integer!'


n=input('give me number n ')
print fibonacci_rec(n)
#even we use "long",n still can't be too big !

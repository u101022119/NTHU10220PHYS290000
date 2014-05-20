#8.factorial_rec.py
def factorial_rec(n):
    if n==0:
        return 1
    if n>0 and (type(n)==int or long):
        return n*factorial_rec(n-1)
    else:
        print 'Wrong!n should be positive integer!'



n=input('give me number n ')
print factorial_rec(n)
#even we use "long",n still can't be too big !

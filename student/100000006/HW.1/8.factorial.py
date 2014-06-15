

def factorial_rec (X):
    X = int(X)
    if X <= 1:
        return 1
    else: return factorial_rec(X-1)*X

print "0! = ",factorial_rec(0)
print "1! = ",factorial_rec(1)
print "2! = ",factorial_rec(2)
print "3! = ",factorial_rec(3)
print "4! = ",factorial_rec(4)

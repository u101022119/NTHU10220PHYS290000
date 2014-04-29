#Homework 2 Exercise: Catalan numbers
def c(n):
    if n ==0:
        return 1
    elif n >= 0:
        return (4 * n - 2) / (n + 1) * c(n - 1)

n = 0
while c(n) <= 1000000:
    print c(n)
    n = n + 1

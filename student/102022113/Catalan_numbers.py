N = 1000000000

def catalan(n):
    if n==0:
        return 1
    else:
        return (4*n-2)*catalan(n-1)/(n+1)

def print_catalan(n):
    if catalan(n)<=N:
        print catalan(n)
        n=n+1
        return print_catalan(n)

print_catalan(0)

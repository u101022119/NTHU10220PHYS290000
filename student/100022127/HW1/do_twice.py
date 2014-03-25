def do_twice(f):
    f()
    f()

def print_spam():
    print'spam'

def do_n(f, n):
    if n<=1:
        f()
    else:
        f()
        do_n(f,n-1)

def print_twice(f):
    print f
    print f

def do_four(f):
    do_twice(f)
    do_twice(f)

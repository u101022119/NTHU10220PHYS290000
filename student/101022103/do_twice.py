1.
def do_twice(f):
    f()
    f()

def print_spam():
    print 'spam'

print do_twice(print_spam)

2.
def do_twice_prime(p, x):
    p()
    p()

3.
def i():
    print 'spam'

def print_twice(i):
    i()
    i()

4.
print do_twice(print_twice)

5.
def do_four(q,y):
    do_twice(q)
    do_twice(q)


    


def print_spam():
    print 'spam'
def do_twice(f):
    f()
    f()
do_twice(print_spam)

def p(x):
    print 5*x+6
def do_twice_2(f,x):
     f(x)
     f(x)
def do_four(f,x):
    f(x)
    f(x)
    f(x)
    f(x)

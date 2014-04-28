def do_twice(f):
    f()
    f()
    
def print_spam():
    print 'spam'
    
do_twice(print_spam)

def do_twice(h):
    h()
    h()

def print_twice():
    print 'spam'

do_twice(print_twice)

def do_four(do_twice):
    do_twice(print_spam)
    do_twice(print_spam)

do_four(do_twice)

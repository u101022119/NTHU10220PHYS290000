def do_twice(f):
    f()
    f()

def print_hello():
    print 'hello'

do_twice(print_hello)

def do_twice(h):
    h()
    h()

def print_twice():
    print 'hello'

do_twice(print_twice)

def do_four(do_twice):
    do_twice(print_hello)
    do_twice(print_hello)
 
do_four(do_twice)

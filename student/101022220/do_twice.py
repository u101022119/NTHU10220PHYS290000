

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

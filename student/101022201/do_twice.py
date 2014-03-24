def do_twice(f):
    f()
    f()

def print_ImHS():
    print 'HS'

do_twice(print_ImHS)

def do_twice(h):
    h()
    h()

def print_twice():
    print '>//<'

do_twice(print_twice)

def do_four(do_twice):
    do_twice(print_twice)
    do_twice(print_twice)
 
do_four(do_twice)




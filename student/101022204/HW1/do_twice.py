def do_twice(f):
    f()
    f()

def print_twice():
    print 'twice'

print do_twice(print_twice)

def do_four(f):
    do_twice(f)
    do_twice(f)

print do_four(print_twice)


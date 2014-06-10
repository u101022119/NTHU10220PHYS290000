def do_twice(f,a):
    f(a)
    f(a)

def print_twice(str):
    print str
    print str

def do_four(f,a):
    do_twice(f,a)
    do_twice(f,a)

def triple(a):
    print a*3


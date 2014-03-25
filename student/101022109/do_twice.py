def do_four(f1,f2,s):
    f1(f2,s)
    f1(f2,s)


def do_twice(f,s):
    f(s)
    f(s)


def print_twice(s):
    print s
    print s


do_four(do_twice,print_twice,'spam')

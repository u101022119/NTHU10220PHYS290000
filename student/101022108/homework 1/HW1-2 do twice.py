def do_twice(f, s):
    f(s)
    f(s)
def print_twice(s):
    print s
    print s
def do_four(f,s):
    do_twice(f,s)
    do_twice(f,s)


s = raw_input()
do_four(print_twice , s)



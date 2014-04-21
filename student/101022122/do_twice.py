def do_twice(f,x):
    f(x)
    f(x)

def print_twice(x):
    print x
    print x

x=raw_input('enter a word:')
do_twice(print_twice,x)

def do_four(f1,f2,x):
    f1(f2,x)
    f1(f2,x)

do_four(do_twice,print_twice,x)

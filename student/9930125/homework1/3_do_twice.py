s = str(raw_input('ENTER A WORD TO DO IT TWICE: '))

def do_twice(f):
    f()
    f()

def print_s():
    print s

def do_four(do_twice):
    do_twice(print_s)
    do_twice(print_s)

do_four(do_twice)

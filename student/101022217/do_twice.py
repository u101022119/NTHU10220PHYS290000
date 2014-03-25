wow = str(raw_input('enter a word to do it twice: '))

def do_twice(f):
    f()
    f()

def print_wow():
    print'wow'
    
def do_four(do_twice):
    do_twice(print_wow)
    do_twice(print_wow)

do_four(do_twice)

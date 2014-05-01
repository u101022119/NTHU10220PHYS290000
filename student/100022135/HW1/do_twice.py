spam = str(raw_input('enter a word to do it twice: '))

def do_twice(f):
    f()
    f()

def print_spam():
    print'spam'
    
def do_four(do_twice):
    do_twice(print_spam)
    do_twice(print_spam)

do_four(do_twice)

def do_twice(f):
    f()
    f()
def print_spam():
    print 'spam'

do_twice(print_spam)

def modified_do_twice(print_twice):
    print_twice()
    print_twice()

def print_twice():
    print 'spam'
    
modified_do_twice(print_twice)

def do_four(do_twice):
   do_twice(print_twice)
   do_twice(print_twice)

do_four(do_twice)


    

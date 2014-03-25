def do_twice(f):
    f()
    f()
def print_spam():
    print "spam"
    
def print_twice(f):
    print f
    print f
def do_four(f):
    print_twice(f)
    print_twice(f)
    
    

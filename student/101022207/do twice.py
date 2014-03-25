def do_twice(f):
    f()
    f()


def print_spam():
    print 'spam'
    print 'spam'
do_twice(print_spam)
################################


def print_twice(v):
    print v
    print v
print_twice('wow')

################################

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_hi():
    print 'hi'
do_four(print_hi)

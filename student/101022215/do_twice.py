def do_twice(f):
    f()
    f()


def print_spam():
    print 'spam'
    print 'spam'
do_twice(print_spam)
################################


def print_twice(a):
    print a
    print a
print_twice('spam')

################################

def do_four(f):
    f()
    f()
    f()
    f()

def print_fxck():
    print 'fxck'
do_four(print_fxck)


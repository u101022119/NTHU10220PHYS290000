def do_twice(f):
    f()
    f()
def print_spam():
    print 'spam'
    
do_twice(print_spam)


def do_twice(d):
    d()
    d()
def print_spam():
    print 'spam'

do_twice(print_spam)
  

def do_four(f):
    do_twice(f)
    do_twice(f)
def print_handsome():
    print 'handsome'

do_four(print_handsome)

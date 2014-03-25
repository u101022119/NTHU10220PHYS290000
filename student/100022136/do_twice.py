#def do_twice(f):
#    f()
#    f()
#def print_spam():
#    print 'spam'
#do_twice(print_spam)
def do_twice(f, s):
    f(s)
    f(s)
def print_twice(s):
    print s
    print s
do_twice(print_twice, 'spam')
def do_four(f, s):
    do_twice(f, s)
    do_twice(f, s)
def print1(s):
    print s
do_four(print1, 'HelloWorld')

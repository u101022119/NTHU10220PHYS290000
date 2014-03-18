def do_twice(f):
    f()
    f()

def print_spam():
    print 'spam'

def print_twice(s):
    print s
    print s

do_twice(print_spam)
print_twice('spam')

#-----1-----

def do_twice(f):
    f()
    f()

def print_spam():
    print 'spam'

do_twice(print_spam)

#-----2-----

def do_twice_m(f,x):
    f(x)
    f(x)

def y(t):
    print t*2

do_twice_m(y,3)

#-----3-----

def print_twice(s):
    print s
    print s

print_twice('hey')

#-----4-----

do_twice_m(print_twice,'spam')

#-----5-----

def do_four(f,x):
    do_twice_m(f,x)
    do_twice_m(f,x)

do_four(y,9)

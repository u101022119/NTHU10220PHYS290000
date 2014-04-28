def do_twice(f):
    f()
    f()

def print_spam():
    print "spam"

print "Demostration of do_twice(print_spam)\n"
do_twice(print_spam)

def do_twice_modified(function, value):
    function(value)
    function(value)

def print_twice(string):
    print string
    print string

print "Demostration of do_twice_modified(print_twice,""spam"")\n"
do_twice_modified(print_twice,"spam")

def do_four(function, value):
    do_twice_modified(function, value)
    do_twice_modified(function, value)

print "Demostraion of do_four(print_twice,""Do it four"")\n"
do_four(print_twice,"Do it four")


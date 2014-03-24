def do_twice(f):
    f()
    f()

def print_spam():
    print "spam"

do_twice(print_spam)

#########################################

def do_twice(f, a):
    f(a)
    f(a)
    return
    
#########################################

def print_twice(a):
    print a
    print a
    return
    

#########################################

do_twice(print_twice,"spam")



#########################################

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)

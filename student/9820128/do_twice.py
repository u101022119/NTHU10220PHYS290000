def do_twice(f,x):             # homework#1_exercise3_2
    f(x)
    f(x)

def print_twice(s):            #homework#1_exercise3_3
    print s
    print s

do_twice(print_twice,'spam')    #homework#1_exercise3_4

def do_four(f,x):             #homework#1_exercise3_5
    do_twice(f,x)
    do_twice(f,x)


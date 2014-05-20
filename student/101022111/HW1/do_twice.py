a = str(raw_input('write down your word:'))
def do_twice(f):
    f()
    f()
def print_spam():
    print a
do_twice(print_spam)

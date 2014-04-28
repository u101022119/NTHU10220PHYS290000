spam = str(raw_input('enter a word to do twice: '))

def do_twice(f):
    f()
    f()

def print_spam():
    print'spam'  ##這裡好怪  它只會輸出spam  所以spam變成字串而不是value?
    
def do_four(do_twice):
    do_twice(print_spam)
    do_twice(print_spam)

print do_four(do_twice)

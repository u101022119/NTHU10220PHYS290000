def print_twice(s):
  print s
  print s

def do_twice(f,v):
  f(v)
  f(v)


def do_four(f,v):
  do_twice(f,v)
  do_twice(f,v)


print 'Call "do_twice"'
do_twice(print_twice,'spam')

print 'Call "do_four"'
do_four(print_twice,'spam')

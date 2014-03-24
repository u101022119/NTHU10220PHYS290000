def right_justify():
    s = str(raw_input('please enter a word to right justify: '))
    a = len(s)
    b = 70 - a
    print " "*b + s

right_justify()



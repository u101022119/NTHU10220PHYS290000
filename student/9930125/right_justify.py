def right_justify():
    s = str(raw_input('PLEASE ENTER A WORD TO RIGHT JUSTIFY: '))
    a = len(s)
    b = 70 - a
    print " "*b , s

right_justify()

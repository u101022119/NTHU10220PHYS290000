
def right_justify():
    s=str(raw_input('enter a word to right justify:'))
    a=len(s)
    b=70-a
    print ' '*b,s

right_justify()

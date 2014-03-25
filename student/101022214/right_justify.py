def right_justify (s):
    mylen = 70
    s1 = str(s)
    for i in range(mylen-len(s)):
        s1 = ' ' + s1
    print s1
    return

right_justify('Evan')

right_justify('asd')


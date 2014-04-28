def right_justify():
    space=' '
    word = str(raw_input('write down your word:'))
    s=space*(70-len(word))+word
    print s



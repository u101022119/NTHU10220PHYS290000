def rightJustify(str):
    for i in range(70-len(str)):
        print '',
    print str


rightJustify("right_justify")
rightJustify("0123456789112345678921234567893123456789412345678951234567896123456789")

def right_justify():
    while raw_input('Exit? Type y.')!='y':
        y=raw_input('type here...=s')
        x=len(y)
        print (70-x)*' ',y
        
right_justify()

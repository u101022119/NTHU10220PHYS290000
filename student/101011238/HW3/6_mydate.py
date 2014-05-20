
class Date(object):
    """Date"""

date1 = Date()
date1.year = 2020
date1.month = 2
date1.day = 28

def print_date(date):
    print '%.4d - %.2d - %.2d' % ( date.year, date.month, date.day)

def increment_date( date, n):
    
    
    while n > 0:
        if date.month == 2:
            date.day += 1
            if date.year % 400 == 0:
                if date.day == 30:
                    date.month += 1
                    date.day = 1
            elif date.year % 100 == 0:
                if date.day == 29:
                    date.month += 1
                    date.day = 1
            elif date.year % 4 == 0:
                if date.day == 30:
                    date.month += 1
                    date.day = 1
            else:
                if date.day == 29:
                    date.month += 1
                    date.day = 1
                    
        elif date.month in ( 1, 3, 5, 7, 8, 10, 12 ):
            date.day += 1
            if date.day == 32:
                date.month += 1
                date.day = 1
                if date.month == 13:
                    date.year += 1
                    date.month = 1            
            
            
        elif date.month in ( 4, 6, 9, 11 ):
            date.day += 1
            if date.day == 31:
                date.month += 1
                date.day = 1
    
        n -= 1

    print_date(date1)




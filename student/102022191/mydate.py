class Date(object):
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day

def is_leap_year(year):
	if year % 4 == 0 and year % 100 !=0 :
		return True
	if year % 400 == 0:
		return True
	return False

def days_of_year(year):
	if is_leap_year(year):
		return 366
	return 365

def date_to_days(date):	
	days = [31,28,31,30,31,30,31,31,30,31,30,31]
	if is_leap_year(date.year):
		days[1] = 29
	tot = 0
	for i in range(date.month-1):
		tot += days[i]
	tot += date.day
	return tot

def days_to_date(year,tot):	
	days = [31,28,31,30,31,30,31,31,30,31,30,31]
	if is_leap_year(year):
		dyas[1] = 29
	month = 0
	while tot > days[month]:
		tot -= days[month]
		month += 1
	month += 1
	return month, tot

def increment_date(date, n):
	year = date.year
	days = date_to_days(date) + n 
	while days_of_year(year) < days:
		days -= days_of_year(year)
		year +=1
	month, day = days_to_date(year, days)
	return Date(year,month,day)

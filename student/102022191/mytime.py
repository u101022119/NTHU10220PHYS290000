class Time(object):
	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second
	def cal_tot(self):
		return self.hour*3600 + self.minute*60 + self.second

def cal_hms(tot):
	m, s = divmod(tot, 60)
	h, m = divmod(m, 60)
	return (h,m,s)

def print_time(t):
	print "%.2d:%.2d:%.2d" %(t.hour, t.minute, t.second)

def is_after(t1,t2):
	return t1.cal_tot()>t2.cal_tot()

def increment_modifier(t, increment):
	tot = t.cal_tot() + increment
	h,m,s = cal_hms(tot)
	t.second = s
	t.minute = m
	t.hour = h

def increment_pure(t,increment):
	tot = t.cal_tot() + increment
	h,m,s = cal_hms(tot)
	return Time(h,m,s)

def mul_time(t,c):
	tot = t.cal_tot() * c
	h,m,s = cal_hms(tot)
	return Time(h,m,s)

def average_pace(t,d):
	reciprocal = 1.0 / d
	ave_pace = mul_time(t,reciprocal)
	return ave_pace

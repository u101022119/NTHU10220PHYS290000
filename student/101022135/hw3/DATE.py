Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 	class Date(object):
	    def print_date(self):
	        print '%d/%.2d/%.2d' % (self.year,self.month,self.day)
	        
   def increment_date(self,date):
      self.day += date
      while True:
          if self.year%4 == 0 and self.month == 2 :
              if self.day > 29:
                  self.day -= 29
                  self.month += 1
              else:
                  break
          elif self.month <8:
              if self.month % 2 == 1:
                  if self.day > 31:
                      self.day -= 31
                      self.month += 1
                  else:
                      break
              elif self.month == 2:
                  if self.day > 28:
                      self.day -=28
                      self.month += 1
                  else:
                      break
              else:
                  if self.day > 30:
                      self.day -= 30
                      self.month += 1
                  else:
                      break
          else:
              if self.month == 12:
                  if self.day > 31:
                      self.day -= 31
                      self.month = 1
                      self.year += 1
                  else:
                      break
              elif self.month % 2 == 0:
                  if self.day > 31:
                      self.day -= 31
                      self.month += 1
                  else:
                      break
              else:
                  if self.day >30:
                      self.day -= 30
                      self.month += 1
                  else:
                      break
       print Date.print_date(self)
date = Date()
date.year = 2012
date.month = 2
date.day = 19

Date.increment_date(date,700)

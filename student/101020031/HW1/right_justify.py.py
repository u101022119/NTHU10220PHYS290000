def right_justify (s):
      display = 70
      nb = str(s)
      for i in range(display-len(s)):
          nb = ' ' + nb
      print nb
      return
  
right_justify('the last letter of the string is 70 of the display(column)')
 

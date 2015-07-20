# Project Euler | Problem 17 | Jacob Waters
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used? Do not count spaces or hyphens.
# 21124
# date : 2015.07.17

def lettersIn1To1000():
  print "1 to 9"
  print "3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4 = 36\n"
  print "10 to 19"
  print "3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8 = 70\n"
  print "20 to 99"
  print "10 x (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) + 8x36 = 748"
  print "SUM 1 to 99: 36 + 70 + 748 = 854\n"
  print "100 to 999"
  print "36x1000 + 854x9 + 7x9 + 9x99x10 = 20259\n\n"
  print "854 + 20259 + 11 = 21124"

lettersIn1To1000()

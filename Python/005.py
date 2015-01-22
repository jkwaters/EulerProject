# Project Euler | Problem 5 | Jacob Waters
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 232792560
# date : 2013.12.10

def smallestMultiple():
  # Problem 5
  # 232792560
  n = 2520
  divide = True
  
  while divide:
    n += 1
    divide = False
    
    for i in range(1,21):
      if n % i != 0:
        divide = True
    if n % 1000000 == 0:
      print n
  
  print n
# smallestMultiple()
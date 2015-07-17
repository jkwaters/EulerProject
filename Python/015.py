# Project Euler | Problem 15 | Jacob Waters
# Starting in the top left corner of a 20×20 grid, and only being able to move to the right and down,
# How many routes are there through the grid? 
# date : 2015.01.26

import math

def powerDigitSum(n,m):
  '''I learned the solution to this problem from an example in Discrete Structures II (COMP 2804)'''
  return math.factorial(n+m)/(math.factorial(n)*math.factorial(n))

print powerDigitSum(20,20)

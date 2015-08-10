# Project Euler | Problem 15 | Jacob Waters
# Starting in the top left corner of a 20x20 grid, and only being able to
# move to the right and down, how many routes are there through the grid?
# 137846528820
# date : 2015.01.26
# I recalled the solution to this problem from an example in class,
# Discrete Structures II (COMP 2804)

import math


def powerDigitSum(n, m):
    return math.factorial(n+m)/(math.factorial(n)*math.factorial(n))


print powerDigitSum(20, 20)

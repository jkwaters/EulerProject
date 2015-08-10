# Project Euler | Problem 20 | Jacob Waters
# Find the sum of the digits in the number 100!
# 648
# date : 2015.07.20

import math


def factorialDigitSum(n):
    return sum([int(i) for i in str(math.factorial(n))])


print factorialDigitSum(100)

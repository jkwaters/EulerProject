# Project Euler | Problem 16 | Jacob Waters
# What is the sum of the digits of the number 2^1000?
# date : 2015.01.26


def powerDigitSum(n, m):
    return sum([int(i) for i in str(n**m)])


print powerDigitSum(2, 1000)

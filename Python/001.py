# Project Euler | Problem 1 | Jacob Waters
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# 233168
# date : 2013.12.10


def problem1(n):
    sum = 0
    for i in xrange(0, n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print problem1(1000)

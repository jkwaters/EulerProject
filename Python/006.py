# Project Euler | Problem 6 | Jacob Waters
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.
# 25164150
# date : 2013.12.10


def sumSquareDiff():
    sumOfSquare = 0
    sum = 0
    for i in range(1, 101):
        sumOfSquare += i**2
        sum += i
    squareOfSum = sum**2
    return squareOfSum - sumOfSquare

print sumSquareDiff()

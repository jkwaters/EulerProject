# Project Euler | Problem 2 | Jacob Waters
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.
# 4613732
# date : 2013.12.10


def evenFibonacciSum(n):
    sum = 2
    nextTerm = 0
    term1 = 1
    term2 = 2

    while(nextTerm < n):
        if nextTerm % 2 == 0:
            sum += nextTerm
        nextTerm = term1 + term2
        term1 = term2
        term2 = nextTerm
    return sum

print evenFibonacciSum(4000000)

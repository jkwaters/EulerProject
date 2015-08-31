# Project Euler | Problem 3 | Jacob Waters
# What is the largest prime factor of the number 600851475143?
# 6857
# date : 2013.12.10


def largestPrimeFactor(n):
    largestFact = 0

    i = 2
    while (i*i <= n):
        if (n % i == 0):
            n = n / i
            largestFact = i
        else:
            i = 3 if i == 2 else i+2

    if (n > largestFact):  # the remainder is a prime number
        largestFact = n

    return largestFact


print largestPrimeFactor(600851475143)

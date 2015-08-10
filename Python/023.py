# Project Euler | Problem 23 | Jacob Waters
# Find the sum of all the positive integers which cannot be
# written as the sum of two abundant numbers.
# 4179871
# date : 2015.07.22


def nonAbundantSums(n):
    sum = 0
    sieve = [True] * (n+1)

    abundant = []
    for x in xrange(1, n):
        if(sumOfFactors(x) > x):
            abundant.append(x)

    for i in xrange(0, len(abundant)):
        for j in xrange(i, len(abundant)):
            if (abundant[i] + abundant[j] <= n):
                # print abundant[i] + abundant[j]
                sieve[abundant[i] + abundant[j]] = False
            else:
                break

    for x in xrange(0, len(sieve)):
        if(sieve[x] is True):
            sum += x

    return sum


def sumOfFactors(n):
    sum = 1
    sqrtN = int(n**0.5)

    if (n == 1):
        return 1

    if(n == (sqrtN*sqrtN)):
        sum += sqrtN
        sqrtN -= 1

    for x in xrange(2, sqrtN+1):
        if (n % x == 0):
            sum += x + (n/x)

    return sum


print nonAbundantSums(28123)
